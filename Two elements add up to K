This problem was recently asked by Google. Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

const isAddingTo = require("./template");

// Testes usando Jest
test('10, 15, 3 and 7 is adding to 17', () => {
    const elements = [10, 15, 3, 7];
    expect(isAddingTo(elements, 17)).toBe(true);
  });
  
  test('17, 15, 3 and 7 is adding to 17', () => {
    const elements = [17, 15, 3, 7];
    expect(isAddingTo(elements, 17)).toBe(false);
  });

function isAddingTo(elements, target) {
    let existingElements = new Set();

    for (let element of elements) {
        const perfectMatch = target - element;
        if (existingElements.has(perfectMatch)) {
            return true;
        }
        existingElements.add(element);
    }

    return false; // Se não encontrou nenhuma soma válida, retorna falso
}
