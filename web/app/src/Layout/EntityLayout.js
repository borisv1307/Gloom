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
        // TODO: Initialize hexagons with enums, currently all the entities are called temp with no images
        const hexagons = GridGenerator.parallelogram(-1, 1, -1, 2).map((hexagon, index) => {
                return Object.assign({}, hexagon, {
                        text: "Temp"
                    }
                );
            }
        )
        this.state = {hexagons};
    }

    onDrop(event, source, targetProps) {
        const {hexagons} = this.state;
        const hexes = hexagons.map(hex => {
            // When hexagon is dropped on this hexagon, copy it's image and text
            if (HexUtils.equals(source.state.hex, hex)) {
                hex.image = targetProps.data.image;
                hex.text = targetProps.data.text;
            }
            return hex;
        });
        this.setState({hexagons: hexes});
    }

    onDragStart(event, source) {
        // Could do something on onDragStart as well, if you wish
    }

// Decide here if you want to allow drop to this node
    onDragOver(event, source) {
        // Find blocked hexagons by their 'blocked' attribute
        const blockedHexes = this.state.hexagons.filter(h => h.blocked);
        // Find if this hexagon is listed in blocked ones
        const blocked = blockedHexes.find(blockedHex => {
            return HexUtils.equals(source.state.hex, blockedHex);
        });

        const {text} = source.props.data;
        // Allow drop, if not blocked and there's no content already
        if (!blocked && !text) {
            // Call preventDefault if you want to allow drop
            event.preventDefault();
        }
    }

// onDragEnd you can do some logic, e.g. to clean up hexagon if drop was success
    onDragEnd(event, source, success) {
        if (!success) {
            return;
        }
        const {hexagons} = this.state;
        // TODO Drop the whole hex from array, currently somethings wrong with the patterns
        // const hexas = hexagons.filter(hex => !HexUtils.equals(targetHex, hex));
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
