import React, {Component} from 'react';
import PerksData from './perks.json';

class Perks extends Component {
    constructor(props) {
        super(props);
        const HARDCODED_CHARACTER = "Brute";
        this.state = {
            "original_cards": ["0", "0", "0", "0", "0", "0", "+1", "+1", "+1", "+1", "+1", "-1", "-1", "-1", "-1", "-1", "+2", "-2", "2x", "Null"],
            "cards": ["0", "0", "0", "0", "0", "0", "+1", "+1", "+1", "+1", "+1", "-1", "-1", "-1", "-1", "-1", "+2", "-2", "2x", "Null"],
            "character": HARDCODED_CHARACTER,
            "perks": PerksData[HARDCODED_CHARACTER],
            "enabled_perks": []
        };
        this.performActions();
    }

    togglePerk(perk_id) {
        let enabled = this.state.enabled_perks;
        let new_enabled = null;
        let perk_index = enabled.indexOf(perk_id);
        if (perk_index === -1) {
            new_enabled = enabled.concat(perk_id);
        } else {
            enabled.splice(perk_index, 1);
            new_enabled = enabled;
        }
        this.setState({
            "enabled_perks": new_enabled
        });
    }

    performActions() {
        for (let perk_id in this.state.perks) {
            if (!this.isPerkEnabled(perk_id)) {
                continue;
            }
            let current_perk = this.state.perks[perk_id];
            for (let action_id in current_perk.actions) {
                let action = current_perk.actions[action_id];
                this.handleAction(action);
            }
        }
    }

    isPerkEnabled(perk_id) {
        // console.log("Enabled Perks: " + this.state.enabled_perks);
        // console.log("Checking perk_id: " + perk_id + " which is: " + (this.state.enabled_perks.indexOf(perk_id) !== -1));
        return this.state.enabled_perks.indexOf(perk_id) !== -1;
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
        this.updateCardState(new_cards);
    }

    handleAdd(card_value) {
        const new_cards = this.state.cards.concat(card_value);
        this.updateCardState(new_cards);
    }

    updatePerkState(new_perk_state) {
        this.setState({
            perks: new_perk_state
        })
    }

    updateCardState(new_cards) {
        this.setState({
            cards: new_cards
        })
    }


    render() {
        // this.resetCards();
        // this.performActions();
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
                    {this.state.cards.map((card, iter) => (
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

    resetCards() {
        this.setState({
            "cards": this.state.original_cards
        })
    }
}

class ToggleablePerk extends Component {
    constructor(props) {
        super(props);
        this.state = {
            "checked": this.props.checked,
            "description": this.props.description,
            "callback": this.props.callback,
            "id": this.props.id
        };
    }

    render() {
        return (
            <div>
                <input type="checkbox"
                    // checked={this.state.checked}
                       onChange={() => this.state.callback(this.state.id)}
                />
                <label htmlFor={'checkbox-' + this.state.key}>{this.state.description}</label>
            </div>
        );
    }
}

export default Perks;
