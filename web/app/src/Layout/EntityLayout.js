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
        const EntityImageEnum = Object.freeze({
            character: "https://img.icons8.com/color/96/000000/morty-smith.png",
            monster: "https://img.icons8.com/color/96/000000/monster-face.png",
            wall: "https://img.icons8.com/color/96/000000/brick-wall.png",
            obstacle: "https://img.icons8.com/color/96/000000/roadblock.png",
            trap: "https://img.icons8.com/color/96/000000/naval-mine.png",
            empty: "",
            hazard: "https://img.icons8.com/color/96/000000/self-destruct-button--v1.png",
            dangerous: "https://img.icons8.com/color/96/000000/error.png"
        });

        var name_values = Object.values(EntityEnum);
        var image_values = Object.values(EntityImageEnum);

        const hexagons = GridGenerator.parallelogram(-1, 0, -1, 2).map((hexagon, index) => {
                return Object.assign({}, hexagon, {
                        text: name_values[index],
                        image: image_values[index]
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
                            {hex.image && <Pattern id={HexUtils.getID(hex)} link={hex.image}/>}
                        </Hexagon>
                    ))
                }
            </Layout>
        );
    }
}

export default EntityLayout;
