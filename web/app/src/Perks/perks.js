import React, {Component} from 'react';
import PerksData from './perks.json';

class Perks extends Component {
    constructor(props) {
        super(props);
        const HARDCODED_CHARACTER = "Brute";
        this.state = {
            "cards": ["+1", "-1"],
            "character": HARDCODED_CHARACTER,
            "perks": PerksData[HARDCODED_CHARACTER]
        }
        this.performActions();
    }

    performActions() {
        for (let perk_id in this.state.perks) {
            let current_perk = this.state.perks[perk_id];
            for (let action_id in current_perk.actions) {
                let action = current_perk.actions[action_id];
                this.handleAction(action);
            }
        }
    }

    handleAction(action) {
        const card_value = action.card;
        switch (action.type) {
            case "REMOVE":
                this.handleRemove(card_value);
                break;
            case "ADD":
                this.handleAdd(card_value);
                break;
            default:
                break;
        }
    }

    handleRemove(card_value) {
        const card_index = this.state.cards.indexOf(card_value);
        const new_cards = this.state.cards.splice(card_index, 1);
        this.updateState(new_cards);
    }

    handleAdd(card_value) {
        const new_cards = this.state.cards.concat(card_value);
        this.updateState(new_cards);
    }

    updateState(new_cards) {
        this.state.cards = new_cards;
    }


    render() {
        return (
            <div>
                <div>CARDS:</div>
                <ul>
                    {this.state.cards.map((card, iter) => (
                        <li key={iter}>{card}</li>
                    ))}
                </ul>
            </div>
        );
    }
}

export default Perks;
