import React, {Component} from 'react'
import './AttackModifier.css'

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
            <div className="attack-deck">
                <div>{this.props.name}</div>
                <div>{cards}</div>
            </div>
        )
    }
}

class AttackModifier extends Component {

    constructor(props) {
        super(props);
        this.state = {
            "deck": [1, 1, 0, 2],
            "selected": [],
            "discard": [1, 2, -1, -2]
        }
    }

    render() {
        return (
            <div>
                <Deck name="discard" cards={this.state.discard} hidden={false}/>
                <Deck name="selected" cards={this.state.selected} hidden={false}/>
                <Deck name="deck" cards={this.state.deck} hidden={true}/>
                <button onClick={() => this.randomSelect()}>Random Select</button>
                <button onClick={() => this.reset()}>Shuffle</button>
            </div>
        )
    }

    randomSelect() {
        if (this.state.deck.length === 0) {
            return;
        }
        const random_idx = this.randomIndex(this.state.deck);
        const item = this.state.deck[random_idx];
        const new_discard = this.state.discard.concat(this.state.selected);
        const new_selected = [item];
        const new_deck = this.removeByIndex(this.state.deck, random_idx)

        this.setState({
            "deck": new_deck,
            "discard": new_discard,
            "selected": new_selected
        })

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
        const new_deck = this.state.deck
            .concat(this.state.discard)
            .concat(this.state.selected);

        this.setState({
            "deck": new_deck,
            "discard": [],
            "selected": []
        })
    }
}

function Card(props) {
    return (
        <div className="attack-cards">{props.value}</div>
    )
}


export default AttackModifier