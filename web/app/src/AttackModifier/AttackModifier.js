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
    cards = {
        "discard": [1, 2, -1, -2],
        "deck": [1, 1, 0, 2]
    }

    render() {
        return (
            <div>
                <Deck name="discard" cards={this.cards.discard} hidden={false}/>
                <Deck name="deck" cards={this.cards.deck} hidden={true}/>
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