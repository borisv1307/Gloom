import React, {Component} from 'react';
import PerksData from './perks.json';

class Perks extends Component {
    constructor(props) {
        super(props);
        const HARDCODED_CHARACTER = "Brute";
        this.state = {
            "cards": ["+1", "-1"],
            "character": HARDCODED_CHARACTER,
            "perks": PerksData[HARDCODED_CHARACTER],
            "enabled_perks": []
        };
        this.addCheckedToPerks();
        this.performActions();
    }

    togglePerk(perk_id) {
        let enabled = this.state.enabled_perks;
        let new_enabled = null;
        if (enabled.indexOf(perk_id) == -1) {
            new_enabled = enabled.concat(perk_id);
        } else {
            new_enabled = enabled.splice(perk_id, 1);
        }
        this.setState({
            "enabled_perks": new_enabled
        })
        console.log(this.state.enabled_perks);
    }

    addCheckedToPerks() {
        for (let perk_id in this.state.perks) {
            let current_perk = this.state.perks[perk_id];
            for (let action_id in current_perk.actions) {
                let action = current_perk.actions[action_id];
                action.checked = true;
                this.setState(this.state.perks)
            }
        }
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
        this.updateCardState(new_cards);
    }

    handleAdd(card_value) {
        const new_cards = this.state.cards.concat(card_value);
        this.updateCardState(new_cards);
    }

    updatePerkState(new_perk_state) {
        this.state.perks = new_perk_state;
    }

    updateCardState(new_cards) {
        this.state.cards = new_cards;
    }


    render() {
        return (
            <div>
                <div>PERKS:</div>
                <ul>
                    {this.state.perks.map((perk, iter) => (
                        <ToggleablePerk
                            description={perk.description}
                            callback={i => this.togglePerk(i)}
                            id={iter}
                            key={iter}/>
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
                       checked={this.state.checked}
                       onChange={() => this.state.callback(this.state.id)}
                />
                <label htmlFor={'checkbox-' + this.state.key}>{this.state.description}</label>
            </div>
        );
    }
}

export default Perks;
