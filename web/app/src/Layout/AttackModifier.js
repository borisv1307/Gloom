import React, {Component} from "react";
import './AttackModifier.css';

let blessDiscard = 0;
let curseDiscard = 0;
let toggle = false;
const cardName = {
            "0": "Zero",
            "+1": "Plus One",
            "-1": "Minus One",
            "+2": "Plus Two",
            "-2": "Minus Two",
            "Null": "Null",
            "2x": "Two Times",
            "2xB": "Two Times Bless",
            "0C": "Zero Curse",
};

let cardValue = "";

class AttackModifier extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isToggleOn: true,
			 "decks": {
                "discard": {
                    "cards": [],
                    "isHidden": false
                },
                "selected": {
                    "cards": [],
                    "isHidden": false
                },
                "deck": {
                    "cards": ["0", "0", "0", "0", "0", "0", "+1", "+1", "+1", "+1", "+1", "-1", "-1", "-1", "-1", "-1", "+2", "-2", "2x", "Null"],
                    "isHidden": true
                }
            },
            // "onclick": (deck_name) => this.handleClickDeck(deck_name),
            bless: 10,
            curse: 10
        }
    }

    // handleClickDeck(deck_name) {
    //     if (deck_name === "discard") {
    //         this.reset();
    //         return;
    //     }
    //     this.randomSelect();
    // }

    randomSelect() {
        const [deck, discard, selected] = this.getDecks();
        if (deck.length === 0) {
            return;
        }
        const random_idx = this.randomIndex(deck);
        const item = deck[random_idx];
        const new_discard = discard.concat(selected);
        const new_selected = [item];
        const new_deck = this.removeByIndex(deck, random_idx)

        if(item === "2xB") {
            blessDiscard += 1;
        }

        if(item === "0C") {
            curseDiscard += 1;
        }

        this.setDecks(new_deck, new_discard, new_selected);
    }

    removeByIndex(array, index) {
        return array.filter(function (el, i) {
            return index !== i;
        });
    }

    randomIndex(array) {
        return Math.floor(Math.random() * array.length);
    }

    reset() {
        const [deck, selected, discard] = this.getDecks();

        console.log("Selected before : " + selected);
        console.log("Discard before : " + discard);

        for(let i=0; i<selected.length; i++) {
            if(selected[i] === "2xB"){
                selected.splice(i, 1);
            }
            else if(selected[i] === "0C"){
                selected.splice(i, 1);
            }
        }
        for(let i=0; i<discard.length; i++) {
            if(discard[i] === "2xB"){
                discard.splice(i, 1);
            }
            else if(discard[i] === "0C"){
                discard.splice(i, 1);
            }
        }

        console.log("Selected after : " + selected);
        console.log("Discard after : " + discard);

        let new_deck = deck.concat(selected).concat(discard);
        console.log("New Deck : " + new_deck);

        let currentBless = this.state.bless;
        this.state.bless = currentBless + blessDiscard;
        blessDiscard = 0;

        let currentCurse = this.state.curse;
        this.state.curse = currentCurse + curseDiscard;
        curseDiscard = 0;

        this.setDecks(new_deck, [], [])
    }

    getDecks() {
        const decks = this.state.decks;
        return [decks.deck.cards, decks.selected.cards, decks.discard.cards];
    }

    setDecks(deck, discard, selected) {
        this.setState({
            "decks": {
                "deck": {
                    "cards": deck
                },
                "discard": {
                    "cards": discard
                },
                "selected": {
                    "cards": selected
                }
            }
        })
    }

    onClickBlessPlus() {
        if(this.state.bless >= 0 && this.state.bless <= 10) {
            this.state.bless = this.state.bless - 1;
            this.state.decks["deck"].cards.push("2xB");
            this.setDecks(this.state.decks.deck.cards, this.state.decks.discard.cards, this.state.decks.selected.cards);
            return;
        }
    }

    onClickBlessMinus() {
        if(this.state.bless >= 0 && this.state.bless <=10) {
            for(var i=0; i<this.state.decks["deck"].cards.length; i++) {
                if(this.state.decks["deck"].cards[i] === "2xB"){
                    this.state.decks["deck"].cards.splice(i,1);
                    this.state.bless = this.state.bless + 1;
                    this.setDecks(this.state.decks.deck.cards, this.state.decks.discard.cards, this.state.decks.selected.cards);
                    return;
                }
            }
        }
    }

    onClickCursePlus() {
        if(this.state.curse >= 0 && this.state.curse <= 10) {
            this.state.curse = this.state.curse - 1;
            this.state.decks["deck"].cards.push("0C");
            this.setDecks(this.state.decks.deck.cards, this.state.decks.discard.cards, this.state.decks.selected.cards);
            return;
        }
    }

    onClickCurseMinus() {
        if(this.state.curse >= 0 && this.state.curse <= 10) {
            for(var i=0; i<this.state.decks["deck"].cards.length; i++) {
                if(this.state.decks["deck"].cards[i] === "0C"){
                    this.state.decks["deck"].cards.splice(i,1);
                    this.state.curse = this.state.curse + 1;
                    this.setDecks(this.state.decks.deck.cards, this.state.decks.discard.cards, this.state.decks.selected.cards);
                    return;
                }
            }
        }
    }

    render() {
        const decks_names = ["discard", "selected"];
        const decks = decks_names.map(
            (key, idx) =>
                <Deck
                    key={idx}
                    name={key}
                    cards={this.state.decks[key].cards}
                    onclick={this.state.onclick}
                />
        );

        var cardsLeft = this.state.decks["deck"].cards.length;
        var blessLeft = this.state.bless;
        var curseLeft = this.state.curse;
        return(
            <div>
                <div className="attack-modifier" style={{flexDirection: "row"}}>
                        {decks}
                        <text>Cards Left: {cardsLeft}</text>
                        <button disabled={cardsLeft <= 0} onClick={() => this.randomSelect()}>Pull Card</button>
                        <button onClick={() => this.reset()}>Shuffle</button>
                </div>

                <div className="bless-and-curse">
                <div id="bless" style={{display: 'flex', lineHeight: '40px'}}>
                    <button disabled={blessLeft <= 0} onClick={() => this.onClickBlessPlus()}>+</button>
                    <text>Bless Cards Left: {blessLeft}</text>
                    <button disabled={blessLeft >= 10} onClick={() => this.onClickBlessMinus()}>-</button>
                </div>

                <div id="curse" style={{display: 'flex', lineHeight: '40px'}}>
                    <button disabled={curseLeft <= 0} onClick={() => this.onClickCursePlus()}>+</button>
                    <text>Curse Cards Left: {curseLeft}</text>
                    <button disabled={curseLeft >= 10} onClick={() => this.onClickCurseMinus()}>-</button>
                </div>
            </div>
            </div>
        )
    }
}

class Deck extends Component {
    get_cards() {
        if (this.props.hidden) {
            return this.props.cards.map(
                (val, idx) =>
                    <Card key={idx} fullName={cardName[val]}/>
            );
        }
        return this.props.cards.map(
            (val, idx) =>
                <Card key={idx} value={val} fullName={cardName[val]}> </Card>
        );
    }

    render() {
        let cards = this.get_cards();

        return (
                <div style={{justifyContent:"flex-start"}}
                     className="attack-deck">
                     {/*onClick={() => this.props.onclick(this.props.name)}>*/}
                    <div>{this.props.name}</div>
                    <div style={{display:"flex",flexDirection: "row", flexWrap:"wrap"}}>{cards}</div>
                </div>
        )
    }
}

function Card(props) {
    console.log("Props.value in function card: " + props.value);
    cardValue = props.value;
     console.log("Props in function card: " + props.fullName);
    return (
            <div id="" className="attack-card"
                 onMouseOver={
                     ()=> onMouseOverHandler()
                 }
                 onMouseLeave={() => onMouseLeaveHandler()}
                 // onMouseOver={()=> alert("Over")}
                 // onMouseLeave={()=>alert("Leave")}
                 // onMouseOut={()=> alert("Out")}
                 style={{flexDirection: "row", textAlign: "top"}}>
                {/*{cardValue}*/}
                {toggle? props.fullName : cardValue}
            </div>

    )
}

function onMouseOverHandler(e) {
    toggle = true;
    // alert(toggle);
    // alert(document.getElementById(currentDiv.id));
    // alert("Enter Value = " + cardName[value]);
    // cardValue = cardName[value];
}

function onMouseLeaveHandler(e) {
    // console.log("Exit Value = " + value)
    toggle = false;
    // alert(toggle);
}

function setId() {
    let list = document.getElementsByClassName("attack-card");
    if(list.length > 0) {
        for (let i = 0; i < list.length; i++) {
            list[i].setAttribute("id", "attack-card-" + i);
        }
    }
}

export default AttackModifier;