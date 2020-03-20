import React, {Component} from 'react';
import {HexGrid} from 'react-hexgrid';
import './App.css';
import EntityLayout from "./Layout/EntityLayout";
import HexLayout from "./Layout/HexLayout";
import PlayingCards from "./Layout/PlayingCards";
import Items from "./items";
import ItemSelection from "./itemSelection";

class App extends Component {
    render() {
        return (
            <div className="app">
                <div>
                    <button style={{display: "flex", float: "left"}}
                            onClick={() => window.location.reload(false)}>Change Character
                    </button>
                </div>
                <p>Items: {this.props.itemsSelected}</p>

                {/*<HexLayout/>*/}
                <EntityLayout/>
                <PlayingCards abilityCards={this.props.abilityCards} characterName = {this.props.characterName}/>
            </div>
        );
    }
}

export default App;
