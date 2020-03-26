import React, {Component} from 'react';
import PerksData from './perks.json';
import AttackModifier from "../Layout/AttackModifier";
import AttackModifierDeck from './AttackModifierDeck.json';

class Perks extends Component {
    constructor(props) {
        super(props);
        this.state = {
            "cards": AttackModifierDeck.initial_deck,
            "perks": PerksData[this.props.characterName],
            "enabled_perks": [],
            "showModifiers": false
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
        if (this.state.showModifiers) {
            return (<AttackModifier cards={cards}/>)
        }
        return (
            <div className='attack-modifier'>
                <div>PERKS:</div>
                <div className="perks">
                    <p>
                        {this.state.perks.map((perk, iter) => (
                            this.renderToggleablePerk(perk, iter)
                        ))}
                    </p>
                </div>
                <div>
                    <button type={"submit"} onClick={() => this.submit()}>
                        Submit
                    </button>
                </div>
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

    submit() {
        this.setState({
            "showModifiers": true
        })
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