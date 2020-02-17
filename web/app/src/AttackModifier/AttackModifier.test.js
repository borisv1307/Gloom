import React from 'react';
import {render} from '@testing-library/react';
import AttackModifier from "./AttackModifier";

test('attack-modifiers can be rendered', () => {
    const {container, _} = render(<AttackModifier/>);
    console.log(container);
    expect(container).toBeDefined();
});

test('initial attack-modifiers deck is non-zero length', () => {
    const {container, _} = render(<AttackModifier/>);
    const cards = container.getElementsByClassName('attack-card')
    expect(cards.length).toBeGreaterThan(0);
});
