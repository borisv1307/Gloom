import React, {Component} from 'react';
import {GridGenerator, Layout, Hexagon, Text, Pattern, HexUtils, HexGrid} from 'react-hexgrid';
import './EntityLayout.css';
import axios from 'axios'

const USER_SERVICE_URL = 'http://0.0.0.0:5000/start';

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

class EntityLayout extends Component {
    constructor(props) {
        super(props);

        const hexagons = GridGenerator.parallelogram(-1, 0, -1, 2).map((hexagon, index) => {
                return Object.assign({}, hexagon, {
                        text: name_values[index],
                        image: image_values[index]
                    }
                );
            }
        );

        const hexagons2 = GridGenerator.hexagon(1);

        this.state = {
            hexagons, hexagons2, isFetching: false,
            JSONdata: {
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
                this.setState({JSONdata: response.data, isFetching: false})
                // console.log("First room = " + response.data[0].name)
            })
            .catch(e => {
                this.setState({...this.state, isFetching: false});
            });
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
        const image = this.state.image[tile_value];
        const text = this.state.text[tile_value];
        const tile_key = "room-" + roomID + "-tile-" + tileID;
        const hex_data = {q: tile.x, r: tile.y, s: tile.z, text: {text}, image: {image}};
        const {hexagons2} = this.state.hexagons2;

        return <Hexagon
            key={tileID}
            q={tile.x}
            r={tile.y}
            s={tile.z}
            fill={tileID}
            image={this.state.image[tile_value]}
            text={this.state.text[tile_value]}
            data={hex_data}
            onDragStart={(e, h) => this.onDragStart(e, h)}
            onDragEnd={(e, h, s) => this.onDragEnd(e, h, s)}
            onDrop={(e, h, t) => this.onDrop(e, h, t)}
            onDragOver={(e, h) => this.onDragOver(e, h)}
        >
            <Text>{text}</Text>
            <Pattern id={tileID} link={image} size={{x: 5, y: 5}}/>
        </Hexagon>

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
        console.log(source.props);
        const {text} = source.props;

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
        const gameHexes = this.parseHexagons();
        // map function needs to somehow have a sense of what {hexagons} state is and append the newly generated hexagon
        return (
            <HexGrid width={1300} height={500} viewBox="-50 -50 100 100">
                <Layout className="game" size={{x: 5, y: 5}} flat={true} spacing={1.0} origin={{x: -30, y: 0}}>
                    {
                        gameHexes
                    }
                </Layout>
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
            </HexGrid>
        );
    }
}

export default EntityLayout;
