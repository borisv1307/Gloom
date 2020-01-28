import React, {Component} from 'react';
import {HexGrid} from 'react-hexgrid';
import './App.css';
import EntityLayout from "./Layout/EntityLayout";
import HexLayout from "./Layout/HexLayout";


class App extends Component {
    render() {
        return (
            <div className="app">
                <h1>Drag & drop tiles</h1>
                <HexGrid width={2600} height={1000} viewBox="-50 -50 100 100">
                    <HexLayout/>
                    <EntityLayout/>
                </HexGrid>
            </div>
        );
    }
}

export default App;