import React, {Component} from 'react';
import {HexGrid} from 'react-hexgrid';
import './App.css';
import EntityLayout from "./Layout/EntityLayout";
import HexLayout from "./Layout/HexLayout";
import PlayingCards from "./Layout/PlayingCards";

class App extends Component {
    render() {
        return (
            <div className="app">
                <div>
                    <button style={{display:"flex", float:"left"}} onClick={() => window.location.reload(false)}>Change Character</button>
                </div>
                <h1>Drag & drop</h1>
                <HexGrid width={650} height={250} viewBox="-50 -50 100 100">
                    <HexLayout/>
                    <EntityLayout/>
                </HexGrid>
                <PlayingCards abilityCards={this.props.abilityCards} characterName = {this.props.characterName}/>
            </div>
        );
    }
}

export default App;
