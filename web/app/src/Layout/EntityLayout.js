import React, {Component} from 'react';
import {GridGenerator, Layout, Hexagon, Text, Pattern, HexUtils} from 'react-hexgrid';
import './EntityLayout.css';

class EntityLayout extends Component {
    constructor(props) {
        super(props);

        const EntityEnum = Object.freeze({
            character: "Character",
            monster: "Monster",
            wall: "Wall",
            obstacle: "Obstacle",
            trap: "Trap",
            empty: "Empty",
            hazard: "Hazardous Terrain",
            dangerous: "Dangerous Terrain"
        });
// TODO: Fix color fill issue, currently the value is a string field that doesn't get parsed right for the library
        const EntityImageEnum = Object.freeze({
            character: "#9a2132",
            monster: "#9a2132",
            wall: "#9a2132",
            obstacle: "#9a2132",
            trap: "#9a2132",
            empty: "#9a2132",
            hazard: "#9a2132",
            dangerous: "#9a2132"
        });

        var name_vals = Object.values(EntityEnum);
        var image_vals = Object.values(EntityImageEnum);

        const hexagons = GridGenerator.parallelogram(-1, 1, -1, 2).map((hexagon, index) => {
                return Object.assign({}, hexagon, {
                        text: name_vals[index],
                        image: image_vals[index]
                    }
                );
            }
        );
        this.state = {hexagons};
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

        const hexas = hexagons.map(hex => {
            if (HexUtils.equals(source.state.hex, hex)) {
                hex.text = null;
                hex.image = null;
            }
            return hex;
        });
        this.setState({hexagons: hexas});
    }

    render() {
        const {hexagons} = this.state;
        return (
            <Layout className="tiles" size={{x: 10, y: 10}} flat={true} spacing={1.0} origin={{x: 60, y: -10}}>
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
                            {!!hex.image && <Pattern id={HexUtils.getID(hex)} link={hex.text}/>}
                        </Hexagon>
                    ))
                }
            </Layout>
        );
    }
}

export default EntityLayout;
