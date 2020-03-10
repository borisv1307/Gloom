import React, {Component} from 'react';
import {GridGenerator, Layout, Hexagon, Text, Pattern, HexUtils, HexGrid} from 'react-hexgrid';
import monsters from '../monsters';
import './EntityLayout.css';
import axios from 'axios'

const USER_SERVICE_URL = 'http://127.0.0.1:5000/start';

const name_values = ["Character", "Monster", "Wall", "Obstacle", "Trap", "Empty", "Hazardous Terrain", "Dangerous Terrain"];


class EntityLayout extends Component {
    constructor(props) {
        super(props);

        const legend_hexagons = GridGenerator.parallelogram(-1, 0, -1, 2).map((hexagon, index) => {
                const monster_key = name_values[index].toLowerCase();
                return Object.assign({}, hexagon, {
                        text: name_values[index],
                        image: monsters[monster_key]
                    }
                );
            }
        );


        const game_hexagons = GridGenerator.hexagon(1).map((hexagon, index) => {
            const monster_key = name_values[index].toLowerCase();
            return Object.assign({}, hexagon, {
                text: {},
                image: {}
            });
        }
        );

        this.state = {
            legend_hexagons, game_hexagons, isFetching: false,
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
            }
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
                console.log(response.data)
            })
            .catch(e => {
                this.setState({...this.state, isFetching: false});
            });
    }

    parseHexagons() {
        const data = this.state.JSONdata;
        const room1 = data[0].tiles;
        const tile_keys = Object.keys(room1);
        const game_hexes = tile_keys.map(i =>
            this.generateHexagon(0, i)
        );
        this.state.game_hexagons = game_hexes;
        return game_hexes;
    }

    generateHexagon(roomID, tileID) {
        const tile = this.state.JSONdata[roomID].tiles[tileID];
        const tile_value = tile.value;
        const image = monsters[tile_value];
        const text = tile_value;
        // const tile_key = "room-" + roomID + "-tile-" + tileID;
        const hex_data = {q: tile.x, r: tile.y, s: tile.z, text: {text}, image: {image}};
        // const {hexagons2} = this.state.hexagons2;

        return <Hexagon
            key={tileID}
            q={tile.x}
            r={tile.y}
            s={tile.z}
            fill={tileID}
            image={image}
            text={text}
            data={hex_data}
            onDragStart={(e, h) => this.onDragStart(e, h)}
            onDragEnd={(e, h, s) => this.onDragEnd(e, h, s)}
            onDrop={(e, h, t) => this.onDropGameHexes(e, h, t)}
            onDragOver={(e, h) => this.onDragOver(e, h)}
        >
            <Text>{text}</Text>
            <Pattern id={tileID} link={image} size={{x: 5, y: 5}}/>
        </Hexagon>
    }


    // onDrop(event, destination, source) {
    //     const {game_hexagons} = this.state;
    //     // console.log(game_hexagons);
    //     // return;
    //     const hexes = game_hexagons.map(hex => {
    //         if (this.areHexesEqual(source.hex, hex)) {
    //             console.log("Hexes are equal");
    //             console.log(hex.props);
    //             console.log(destination.props);
    //             // console.log(hex);
    //             // console.log(hex.props);
    //             hex.image = source.hex.image;
    //             hex.text = source.hex.text;
    //         }
    //         return hex;
    //     });
    //     console.log(hexes);
    //     if (hexes) {
    //         this.setState({game_hexagons: hexes});
    //     }
    // }

    // Making a specific onDrop() to handle game hexes
    onDropGameHexes(event, source, targetProps) {
    const {game_hexagons} = this.state;
    const hexes = game_hexagons.map(hex => {
      // When hexagon is dropped on this hexagon, copy it's image and text
      if (this.areHexesEqual(source, hex)) {
        hex.image = targetProps.image;
        hex.text = targetProps.text;
      }
      return hex;
    });
    this.setState({ game_hexagons: hexes });
  }

    areHexesEqual(source, destination) {
        const source_props = source.props;
        const destination_props = destination.props;
        console.log("SOURCE PROPS:");
        console.log(source_props);
        console.log(destination_props);
        console.log("DESTINATION PROPS:");
        console.log(destination_props);
        if (source_props.q !== destination_props.q) {
            return false;
        }
        if (source_props.r !== destination_props.r) {
            return false;
        }
        if (source_props.s !== destination_props.s) {
            return false;
        }
        return true;
    }

    onDragStart(event, source) {
        if (!source.props.data.text) {
            event.preventDefault();
        }
    }

    onDragOver(event, source) {
        if (this.isValidDroppable(event, source)) {
            event.preventDefault();
        }
    }

    // Specifically for legend_hexagons
    onDrop(event, source, targetProps) {
        const {legend_hexagons} = this.state;
        const hexes = legend_hexagons.map(hex => {
          // When hexagon is dropped on this hexagon, copy it's image and text
          if (HexUtils.equals(source.state.hex, hex)) {
            hex.image = targetProps.data.image;
            hex.text = targetProps.data.text;
          }
          return hex;
        });
        this.setState({ legend_hexagons: hexes });
    }

    isValidDroppable(event, source) {
        return true;
        // const blockedHexes = this.state.hexagons.filter(h => h.blocked);
        // const blocked = blockedHexes.find(blockedHex => {
        //     return HexUtils.equals(source.state.hex, blockedHex);
        // });
        // console.log(source.props);
        // const {text} = source.props;
        // console.log(text);
        // return !blocked;
    }

    onDragEnd(event, source, success) {
        if (!success) {
            return;
        }
        const {game_hexagons} = this.state;

        const hexes = game_hexagons.map(hex => {
            if (HexUtils.equals(source.state.hex, hex)) {
                hex.text = null;
                hex.image = null;
            }
            return hex;
        });
        this.setState({game_hexagons: hexes});
    }

    render() {
        const {legend_hexagons} = this.state;
        const game_hexes = this.parseHexagons();
        console.log("Game Hexagons (left)");
        console.log(game_hexes);
        console.log("Legend Hexagons (right)");
        console.log(legend_hexagons);

        // map function needs to somehow have a sense of what {hexagons} state is and append the newly generated hexagon
        return (
            <HexGrid width={1300} height={500} viewBox="-50 -50 100 100">
                <Layout className="game" size={{x: 6, y: 6}} flat={true} spacing={1.0} origin={{x: -30, y: 0}}>
                    {
                        game_hexes
                    }
                </Layout>
                <Layout className="tiles" size={{x: 6, y: 6}} flat={true} spacing={1.0} origin={{x: 60, y: -10}}>
                    {
                        legend_hexagons.map((hex, i) => (
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
