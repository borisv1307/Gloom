import React, {Component} from 'react';
import {HexGrid, Layout, Hexagon, GridGenerator} from 'react-hexgrid';
import './App.css';

class SquareHexGrid extends Component {
    render() {
        const hexagons = GridGenerator.orientedRectangle(4, 4);

        return (
            <HexGrid width={1200} height={1000}>
                <Layout size={{x: 7, y: 7}}>
                    {hexagons.map((hex, i) => <Hexagon key={i} q={hex.q} r={hex.r} s={hex.s}/>)}
                </Layout>
            </HexGrid>
        );
    }
}

class App extends Component {
    render() {
        return (
            <div className="App">
                <h1>Basic example of HexGrid usage.</h1>
                <SquareHexGrid />

            </div>
        );
    }
}

export default App;