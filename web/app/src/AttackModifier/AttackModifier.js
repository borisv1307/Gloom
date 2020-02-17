import React, {Component} from 'react'
import './AttackModifier.css'


class AttackModifier extends Component {
    constructor(props) {
        super(props);
        this.state = {
            "decks": {
                "discard": {
                    "cards": [1, -1, -2, 0],
                    "isHidden": false
                },
                "selected": {
                    "cards": [],
                    "isHidden": false
                },
                "deck": {
                    "cards": [1, 1, 0, 2],
                    "isHidden": true
                }
            },
            "onclick": (deck_name) => this.handleClick(deck_name)
        }
    }

    render() {
        const decks_names = ["discard", "selected", "deck"];
        const decks = decks_names.map(
            (key, idx) =>
                <Deck
                    key={idx}
                    name={key}
                    cards={this.state.decks[key].cards}
                    onclick={this.state.onclick}
                    hidden={this.state.decks[key].isHidden}
                />
        );

        return (
            <div>
                {decks}
                <button onClick={() => this.randomSelect()}>Random Select</button>
                <button onClick={() => this.reset()}>Reset</button>
            </div>
        )
    }

    handleClick(deck_name) {
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
            <div className="attack-deck" onClick={() => this.props.onclick(this.props.name)}>
                <div>{this.props.name}</div>
                <div>{cards}</div>
            </div>
        )
    }
}

function Card(props) {
    return (
        <div className="attack-cards">{props.value}</div>
    )
}


export default AttackModifier