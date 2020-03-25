import React, {Component} from 'react';
import './App.css';
import EntityLayout from "./Layout/EntityLayout";
import PlayingCards from "./Layout/PlayingCards";
import RoomCardImages from "./RoomCardImages"
import MonsterCardImages from "./MonsterCardImages"
import axios from 'axios'

const USER_SERVICE_URL = 'http://127.0.0.1:5000/start';

function showRoomAndMonster(roomID) {

    for (let i = 1; i <= 3; i++) {
        if (i != Number(roomID)) {
            document.getElementById("Room" + i).style.display = "none";
            document.getElementById("discard-pile").style.height = "30em";
        }
    }

    if (document.getElementById("Room" + roomID).style.display === "none") {
        document.getElementById("Room" + roomID).style.display = "flex";
        document.getElementById("discard-pile").style.height = "20em";
    } else {
        document.getElementById("Room" + roomID).style.display = "none";
        document.getElementById("discard-pile").style.height = "30em";
    }
}

class RoomButtons extends Component {

    componentDidMount() {

        for (let roomNumber = 0; roomNumber < 3; roomNumber++) {
            if (this.props.jsonData[roomNumber] !== undefined) {
                let currentRoomNumber = roomNumber + 1;
                document.getElementById("roomButton" + currentRoomNumber).style.display = "flex";
                for (let i = 0; i < RoomCardImages.length; i++) {
                    if (RoomCardImages[i].id === this.props.jsonData[roomNumber].name) {
                        document.getElementById("roomCard" + currentRoomNumber).src = RoomCardImages[i].src;
                    }

                    if (MonsterCardImages[i].id === this.props.jsonData[roomNumber].monsterCardName) {
                        document.getElementById("monsterCard" + currentRoomNumber).src = MonsterCardImages[i].src;
                    }

                }

            }
        }
    }

    render() {
        return (
            <div className="roomButtonComponent">
                <div className="buttonsDiv">
                    <button id="roomButton1" className="roomButton" onClick={() => showRoomAndMonster("1")}>Room1
                    </button>
                    <button id="roomButton2" className="roomButton" onClick={() => showRoomAndMonster("2")}>Room2
                    </button>
                    <button id="roomButton3" className="roomButton" onClick={() => showRoomAndMonster("3")}>Room3
                    </button>
                </div>

                <div id="Room1" className="Room" style={{display: "none", justifyContent: "flex-start"}}>
                    <img name="roomCard" id="roomCard1" src="" alt=""/>
                    <img name="monsterCard" id="monsterCard1" src="" alt=""/>
                </div>
                <div id="Room2" className="Room" style={{display: "none", justifyContent: "flex-start"}}>
                    <img name="roomCard" id="roomCard2" src="" alt=""/>
                    <img name="monsterCard" id="monsterCard2" src="" alt=""/>
                </div>
                <div id="Room3" className="Room" style={{display: "none", justifyContent: "flex-start"}}>
                    <img name="roomCard" id="roomCard3" src="" alt=""/>
                    <img name="monsterCard" id="monsterCard3" src="" alt=""/>
                </div>
            </div>
        )
    }

}

class App extends Component {

    constructor(props) {

        super(props);
        this.state = {
            isFetching: true,
            JSONdata: {
                "0": {
                    "name": "Encampment",
                    "tiles": {
                        "0": {
                            "x": 0,
                            "y": 0,
                            "z": 0,
                            "value": "monster"
                        },
                        "monsterCardName": "cutthroat"
                    }
                }
            }
        };
    }

    componentWillMount() {
        this.fetchDungeonData();
    }

    fetchDungeonData() {
        this.setState({...this.state, isFetching: true});
        axios.get(USER_SERVICE_URL)
            .then(response => {
                this.setState({JSONdata: response.data, isFetching: false})
                // console.log("First room App = " + response.data[0].name)
            })
            .catch(e => {
                this.setState({...this.state, isFetching: false});
            });
    }

    handleSingleCheck(event) {
        if (event.shiftKey)
            event.target.parentElement.parentElement.classList.toggle('selection');
        event.target.parentElement.parentElement.classList.toggle('selection');
    }

    render() {
        let rows = this.props.itemsSelected.map((row) => {
            return (
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
                <br/>
                {
                    this.state.isFetching ? <div/> : <RoomButtons jsonData={this.state.JSONdata}/>
                }
                <div className="item-table">
                    <table>
                        <thead>
                        <tr>
                            <th>Items</th>
                        </tr>
                        </thead>
                        <tbody>
                        {rows}
                        </tbody>
                    </table>
                </div>
                {/*<HexLayout/>*/}
                {
                    this.state.isFetching ? <div/> : <EntityLayout jsonData={this.state.JSONdata}/>
                }
                <PlayingCards abilityCards={this.props.abilityCards} characterName={this.props.characterName}/>
            </div>
        );
    }
}

export default App;
