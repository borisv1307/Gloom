import React, {Component} from "react";
import './AttackModifier.css';

const initial_deck = ["0", "0", "0", "0", "0", "0", "+1", "+1", "+1", "+1", "+1", "-1", "-1", "-1", "-1", "-1", "+2", "-2", "2x", "Null"];

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
            "onclick": (deck_name) => this.handleClickDeck(deck_name),
            bless: 10,
            curse: 10
        }
    }

    handleClickDeck(deck_name) {
        if (deck_name === "discard") {
            this.reset();
            return;
        }
        this.randomSelect();
    }

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
        let new_deck = deck
            .concat(selected)
            .concat(discard);
        console.log("New Deck : " + new_deck);

        new_deck = initial_deck;

        console.log("New Deck After While : " + new_deck);
        this.state.bless = 10;
        this.state.curse = 10;

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
        if(this.state.bless !== 0 && this.state.bless <=10) {
            this.state.bless = this.state.bless - 1;
            this.state.decks["deck"].cards.push("2xB");
            this.setDecks(this.state.decks.deck.cards, this.state.decks.discard.cards, this.state.decks.selected.cards);
            return;
        }
    }

    onClickBlessMinus() {
        if(this.state.bless !== 0 && this.state.bless <=10) {
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
        if(this.state.curse != 0) {
            this.state.curse = this.state.curse - 1;
            this.state.decks["deck"].cards.push("-2C");
            this.setDecks(this.state.decks.deck.cards, this.state.decks.discard.cards, this.state.decks.selected.cards);
            return;
        }
    }

    onClickCurseMinus() {
        for(var i=0; i<this.state.decks["deck"].cards.length; i++) {
            if(this.state.decks["deck"].cards[i] === "-2C"){
                this.state.decks["deck"].cards.splice(i,1);
                this.state.curse = this.state.curse + 1;
                this.setDecks(this.state.decks.deck.cards, this.state.decks.discard.cards, this.state.decks.selected.cards);
                return;
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
                        <button onClick={() => this.randomSelect()}>Pull Card</button>
                        <button onClick={() => this.reset()}>Reset</button>
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
                    <Card key={idx}/>
            );
        }
        return this.props.cards.map(
            (val, idx) =>
                <Card key={idx} value={val}/>
        );
    }

    render() {
        let cards = this.get_cards();

        return (
                <div style={{justifyContent:"flex-start"}}
                     className="attack-deck" onClick={() => this.props.onclick(this.props.name)}>
                    <div>{this.props.name}</div>
                    <div style={{display:"flex",flexDirection: "row", flexWrap:"wrap"}}>{cards}</div>
                </div>
        )
    }
}

function Card(props) {
    return (
        <div className="attack-card" style={{flexDirection: "row", textAlign: "top"}}>
            {props.value}</div>
    )
}

export default AttackModifier;