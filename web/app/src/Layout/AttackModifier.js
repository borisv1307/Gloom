import React, {Component} from "react";
import './AttackModifier.css';

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
            "onclick": (deck_name) => this.handleClickDeck(deck_name)
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
        const new_deck = deck
            .concat(selected)
            .concat(discard);

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


        return(
            <div className="attack-modifier" style={{flexDirection: "row"}}>
                    {decks}
                    <text>Cards Left: {cardsLeft}</text>
                    <button onClick={() => this.randomSelect()}>Pull Card</button>
                    <button onClick={() => this.reset()}>Reset</button>
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