import React, {Component} from 'react';
import {GridGenerator, Layout, Hexagon, Text, Pattern, HexUtils, HexGrid} from 'react-hexgrid';
import monsters from '../monsters';
import './EntityLayout.css';


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


var name_values = ["Character", "Monster", "Wall", "Obstacle", "Trap", "Empty", "Hazardous Terrain", "Dangerous Terrain"];

class EntityLayout extends Component {
    constructor(props) {
        super(props);

        const hexagons = GridGenerator.parallelogram(-1, 0, -1, 2).map((hexagon, index) => {
                const monster_key = name_values[index].toLowerCase();
                return Object.assign({}, hexagon, {
                        text: name_values[index],
                        image: monsters[monster_key]
                    }
                );
            }
        );

        const parsed_hexagons = GridGenerator.hexagon(1);

        this.state = {
            hexagons, parsed_hexagons, isFetching: false,
            JSONdata: this.props.JSONdata,
            image: image,
            text: text
        };
    }

    componentWillMount() {
    }

    parseHexagons() {
        const data = this.state.JSONdata;
        const room1 = data[0].tiles;
        const tile_keys = Object.keys(room1);
        return tile_keys.map(i =>
            this.generateHexagon(0, i)
        )
    }

    generateHexagon(roomID, tileID) {
        const tile = this.state.JSONdata[roomID].tiles[tileID];
        const tile_value = tile.value;
        const image_val = monsters[tile_value];
        const text_val = tile_value;
        const hex_data = {q: tile.x, r: tile.y, s: tile.z, text: {text}, image: {image}};

        return Object.assign({}, {
            image: image_val,
            text: text_val,
            q: tile.x,
            r: tile.y,
            s: tile.z
        });
    }

    onDrop(event, source, targetProps) {
        const {hexagons} = this.state;
        const {parsed_hexagons} = this.state;

        const hexes = hexagons.map(hex => {
            if (HexUtils.equals(source.state.hex, hex)) {
                hex.image = targetProps.data.image;
                hex.text = targetProps.data.text;
            }
            return hex;
        });

        const hexes2 = parsed_hexagons.map(hex2 => {
            if (HexUtils.equals(source.state.hex, hex2)) {
                hex2.image = targetProps.data.image;
                hex2.text = targetProps.data.text;
            }
            return hex2;
        });
        this.setState({hexagons: hexes, parsed_hexagons: hexes2});
    }

    onDragStart(event, source) {
        if (!source.props.data.text) {
            event.preventDefault();
        }
    }

    onDragOver(event, source) {
        const {text} = source.props;
        if (!text) {
            event.preventDefault();
        }
    }

    onDragEnd(event, source, success) {
        if (!success) {
            return;
        }
        const {hexagons} = this.state;
        const {parsed_hexagons} = this.state;

        const hexes = hexagons.map(hex => {
            if (HexUtils.equals(source.state.hex, hex)) {
                hex.text = null;
                hex.image = null;
            }
            return hex;
        });

        const hexes2 = parsed_hexagons.map(hex2 => {
            if (HexUtils.equals(source.state.hex, hex2)) {
                hex2.text = null;
                hex2.image = null;
            }
            return hex2;
        });
        this.setState({hexagons: hexes, parsed_hexagons: hexes2});
    }

    render() {
        const {hexagons} = this.state;
        const gameHexes = this.parseHexagons();

        console.log(gameHexes);
        console.log("--- Static Hexes Below ---");
        console.log(hexagons);

        return (
            <HexGrid width={1300} height={500} viewBox="-50 -50 100 100">
                    <Layout className="game" size={{x: 7.5, y: 7.5}} flat={true} spacing={1.0} origin={{x: -30, y: 0}}>
                        {
                            gameHexes.map((hex, i) => (
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
                                    {!!hex.image && <Pattern id={HexUtils.getID(hex)} link={hex.image}/>}
                                </Hexagon>
                            ))
                        }
                    </Layout>

                <Layout className="tiles" size={{x: 7.5, y: 7.5}} flat={true} spacing={1.0} origin={{x: 70, y: -10}}>
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
                                {!!hex.image && <Pattern id={HexUtils.getID(hex)} link={hex.image}/>}
                            </Hexagon>
                        ))
                    }
                </Layout>
            </HexGrid>
        );
    }
}

export default EntityLayout;