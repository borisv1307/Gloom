import React, {Component} from 'react';
import PerksData from './perks.json';

class Perks extends Component {
    constructor(props) {
        super(props);
        const HARDCODED_CHARACTER = "Brute";
        this.state = {
            "cards": ["0", "0", "0", "0", "0", "0", "+1", "+1", "+1", "+1", "+1", "-1", "-1", "-1", "-1", "-1", "+2", "-2", "2x", "Null"],
            "character": HARDCODED_CHARACTER,
            "perks": PerksData[HARDCODED_CHARACTER],
            "enabled_perks": []
        };
    }

    togglePerk(perk_id) {
        let enabled = this.state.enabled_perks;
        let new_enabled = null;
        let perk_index = enabled.indexOf(perk_id);
        if (perk_index === -1) {
            new_enabled = enabled.concat([perk_id]);
        } else {
            enabled.splice(perk_index, 1);
            new_enabled = enabled;
        }
        this.setState({
            "enabled_perks": new_enabled
        });
    }

    performActions() {
        let cards = Array.from(this.state.cards);
        let perks = this.state.perks;
        for (let perk_id in perks) {
            if (!this.isPerkEnabled(perk_id)) {
                continue;
            }
            let current_perk = perks[perk_id];
            for (let action_id in current_perk.actions) {
                let action = current_perk.actions[action_id];
                cards = this.handleAction(action, cards);
            }
        }
        return cards;
    }

    isPerkEnabled(perk_id) {
        // console.log("Enabled Perks: " + this.state.enabled_perks);
        // console.log("Checking perk_id: " + perk_id + " which is: " + (this.state.enabled_perks.indexOf(parseInt(perk_id, 10)) !== -1));
        return this.state.enabled_perks.indexOf(parseInt(perk_id, 10)) !== -1;
    }

    handleAction(action, cards) {
        const card_value = action.card;
        switch (action.type) {
            case "REMOVE":
                cards = this.handleRemove(card_value, cards);
                break;
            case "ADD":
                cards = this.handleAdd(card_value, cards);
                break;
            default:
                break;
        }
        return cards;
    }

    handleRemove(card_value, cards) {
        const card_index = cards.indexOf(card_value);
        cards.splice(card_index, 1);
        return cards;
    }

    handleAdd(card_value, cards) {
        const new_cards = cards.concat(card_value);
        return new_cards;
    }

    render() {
        let cards = this.performActions();
        return (
            <div>
                <div>PERKS:</div>
                <ul>
                    {this.state.perks.map((perk, iter) => (
                        this.renderToggleablePerk(perk, iter)
                    ))}
                </ul>
                <div>CARDS:</div>
                <ul>
                    {cards.map((card, iter) => (
                        <li key={iter}>{card}</li>
                    ))}
                </ul>
            </div>
        );
    }

    renderToggleablePerk(perk, index) {
        return (
            <ToggleablePerk
                description={perk.description}
                callback={() => this.togglePerk(index)}
                key={index}/>
        )
    }
}


const ToggleablePerk = props => (
    <div>
        <input
            type="checkbox"
            onChange={props.callback}>
        </input>
        <label>{props.description}</label>
    </div>
)

export default Perks;
