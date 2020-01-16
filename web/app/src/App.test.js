import React from 'react';
import { render } from '@testing-library/react';
import SquareHexGrid from './App';

test('renders square hex grid renders a square number of hexagons', () => {
  const { container } = render(<SquareHexGrid />);
  const numHexagons = container.querySelectorAll('.hexagon-group').length;
  const isNumHexagonsAPerfectSquare = numHexagons > 0 && Math.sqrt(numHexagons) % 1 === 0;
  expect(isNumHexagonsAPerfectSquare).toBe(true);
});