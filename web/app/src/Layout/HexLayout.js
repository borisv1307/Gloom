import React, {Component} from 'react';
import {GridGenerator, Layout, Hexagon, Text, Pattern, HexUtils} from 'react-hexgrid';
import './HexLayout.css';
import axios from 'axios'

const USER_SERVICE_URL = 'http://0.0.0.0:5000/start';

class HexLayout extends Component {
    constructor(props) {
        super(props);
        const hexagons = GridGenerator.hexagon(0);
        // this.state = {hexagons};
        this.state = {
            isFetching: false,
            hexagons: []
        };
    }

    componentDidMount() {
        this.fetchHexagons();
    }

    fetchHexagons() {
        this.setState({...this.state, isFetching: true});
        axios.get(USER_SERVICE_URL)
            .then(response => {
                this.setState({data: response.data, isFetching: false})
                console.log(response.data);
            })
            .catch(e => {
                this.setState({...this.state, isFetching: false});
            });
    }

    onDrop(event, source, targetProps) {
        const {hexagons} = this.state;
        const hexes = hexagons.map(hex => {
            if (HexUtils.equals(source.state.hex, hex)) {
                hex.image = targetProps.data.image;
                hex.text = targetProps.data.text;
            }
            return hex;
        });
        this.setState({hexagons: hexes});
    }

    onDragStart(event, source) {
        if (!source.props.data.text) {
            event.preventDefault();
        }
    }

    onDragOver(event, source) {
        const blockedHexes = this.state.hexagons.filter(h => h.blocked);
        const blocked = blockedHexes.find(blockedHex => {
            return HexUtils.equals(source.state.hex, blockedHex);
        });

        const {text} = source.props.data;
        if (!blocked && !text) {
            event.preventDefault();
        }
    }

    onDragEnd(event, source, success) {
        if (!success) {
            return;
        }

        const {hexagons} = this.state;
        const hexes = hexagons.map(hex => {
            if (HexUtils.equals(source.state.hex, hex)) {
                hex.text = null;
                hex.image = null;
            }
            return hex;
        });
        this.setState({hexagons: hexes});
    }

    render() {
        let {hexagons} = this.state;
        return (
            <Layout className="game" size={{x: 10, y: 10}} flat={true} spacing={1.08} origin={{x: -30, y: 0}}>
                {
                    hexagons.map((hex, i) => (
                        <Hexagon
                            key={i}
                            q={hex.q}
                            r={hex.r}
                            s={hex.s}
                            fill={(hex.image) ? HexUtils.getID(hex) : null}
                            data={hex}
                            onDragStart={(e, h) => this.onDragStart(e, h)}
                            onDragEnd={(e, h, s) => this.onDragEnd(e, h, s)}
                            onDrop={(e, h, t) => this.onDrop(e, h, t)}
                            onDragOver={(e, h) => this.onDragOver(e, h)}
                        >
                            <Text>{hex.text}</Text>
                            {hex.image && <Pattern id={HexUtils.getID(hex)} link={hex.image}/>}
                        </Hexagon>
                    ))
                }
            </Layout>
        );
    }
}

export default HexLayout;
