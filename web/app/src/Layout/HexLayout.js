import React, {Component} from 'react';
import {GridGenerator, Layout, Hexagon, Text, Pattern, HexUtils} from 'react-hexgrid';
import './HexLayout.css';
import axios from 'axios'

const USER_SERVICE_URL = 'http://0.0.0.0:5000/start';

class HexLayout extends Component {
    constructor(props) {
        const text = {
            character: "Character",
            monster: "Monster",
            wall: "Wall",
            obstacle: "Obstacle",
            trap: "Trap",
            empty: "Empty",
            hazard: "Hazardous Terrain",
            dangerous: "Dangerous Terrain",
            entrance_a: "Entry A",
            entrance_b: "Entry B",
            "exit a": "Exit A",
            "exit b": "Exit B",
            coin: "Coin"

        };
        const image = {
            character: "https://img.icons8.com/color/96/000000/morty-smith.png",
            monster: "https://img.icons8.com/color/96/000000/monster-face.png",
            wall: "https://img.icons8.com/color/96/000000/brick-wall.png",
            obstacle: "https://img.icons8.com/color/96/000000/roadblock.png",
            trap: "https://img.icons8.com/color/96/000000/naval-mine.png",
            empty: "",
            hazard: "https://img.icons8.com/color/96/000000/self-destruct-button--v1.png",
            dangerous: "https://img.icons8.com/color/96/000000/error.png"
        };

        super(props);
        const hexagons = GridGenerator.hexagon(1);
        this.state = {hexagons};
        this.state = {
            isFetching: false,
            data: {
                "0": {
                    "name": "Den",
                    "tiles": {
                        "0": {
                            "x": 0,
                            "y": 0,
                            "z": 0,
                            "value": "monster"
                        },
                    }
                }
            },
            image: image,
            text: text
        };
    }

    componentWillMount() {
        this.fetchHexagons();
    }

    fetchHexagons() {
        this.setState({...this.state, isFetching: true});
        axios.get(USER_SERVICE_URL)
            .then(response => {
                this.setState({data: response.data, isFetching: false})
                // console.log("First room = " + response.data[0].name)
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
        event.preventDefault();
    }

    onDragOver(event, source) {
        const {text} = source.props.data.text;
        if (!text) {
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

    parseHexagons() {
        const data = this.state.data;
        const room1 = data[0].tiles;
        const tile_keys = Object.keys(room1);

        // map function needs to somehow have a sense of what {hexagons} state is and append the newly generated hexagon
        return tile_keys.map(tileID =>
            this.generateHexagon(0, tileID)
        )
    }

    generateHexagon(roomID, tileID, q, r, s) {
        const tile = this.state.data[roomID].tiles[tileID];
        const tile_value = tile.value;
        const image = this.state.image[tile_value]; // Didn't get set in <Hexagon>
        const text = this.state.text[tile_value]; // Didn't get set in <Hexagon>
        const tile_key = "room-" + roomID + "-tile-" + tileID;

        return <Hexagon
            key={tileID} // Changed to tileID from tile_key
            q={tile.x}
            r={tile.y}
            s={tile.z}
            fill={tileID}
            image={this.state.image[tile_value]}
            text={this.state.text[tile_value]}
            onDragStart={(e, h) => this.onDragStart(e, h)}
            onDragEnd={(e, h, s) => this.onDragEnd(e, h, s)}
            onDrop={(e, h, t) => this.onDrop(e, h, t)}
            onDragOver={(e, h) => this.onDragOver(e, h)}
        >
            <Text>{text}</Text>
            <Pattern id={tileID} link={this.state.image[tile_value]} size={{x: 5, y: 5}}/>
        </Hexagon>

    }

    render() {
        const hexagons = this.parseHexagons();
        // props: key is undefined because it's not mapped correctly?
        console.log(hexagons);
        return (
            <Layout className="game" size={{x: 5, y: 5}} flat={true} spacing={1.08} origin={{x: -30, y: 0}}>
                {hexagons}
            </Layout>
        );
    }
}

export default HexLayout;