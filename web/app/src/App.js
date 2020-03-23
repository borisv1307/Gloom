import React, {Component} from 'react';
import {HexGrid} from 'react-hexgrid';
import './App.css';
import EntityLayout from "./Layout/EntityLayout";
import HexLayout from "./Layout/HexLayout";
import PlayingCards from "./Layout/PlayingCards";

class App extends Component {
    handleSingleCheck(event){
    if(event.shiftKey)
        event.target.parentElement.parentElement.classList.toggle('selection');
    event.target.parentElement.parentElement.classList.toggle('selection');
  }
    render() {
        let rows = this.props.itemsSelected.map((row)=>{
        return(
          <tr>
            <td><input type="checkbox" onClick={this.handleSingleCheck.bind(this)}/></td>
              <td>{row}</td>
          </tr>
        );
    });
        return (
            <div className="app">
                <div>
                    <button style={{display: "flex", float: "left"}}
                            onClick={() => window.location.reload(false)}>Change Character
                    </button>
                </div>
             <div className="item-table">
                <table>
                <thead>
                    <tr>
                    <th>Items</th>
                    </tr>
                </thead>
                <tbody >
                    { rows }
                </tbody>
                </table>
            </div>
                {/*<HexLayout/>*/}
                <EntityLayout/>
                <PlayingCards abilityCards={this.props.abilityCards} characterName = {this.props.characterName}/>
            </div>
        );
    }
}

export default App;
