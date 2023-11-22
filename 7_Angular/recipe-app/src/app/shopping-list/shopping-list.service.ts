import { Ingredient } from '../shared/ingredient.model';
import { Subject } from 'rxjs';

export class ShoppingListService {
  ingredientAdded = new Subject<Ingredient[]>();
  private ingredients: Ingredient[] = [
    new Ingredient('ingredient 1', 1),
    new Ingredient('ingredient 2', 2),
    new Ingredient('ingredient 3', 3),
  ];

  getIngredients() {
    return this.ingredients.slice();
  }

  addIngredient(ingredient: Ingredient) {
    this.ingredients.push(ingredient);
    this.ingredientAdded.next(this.ingredients.slice());
  }
  addIngredients(ingredients: Ingredient[]) {
    this.ingredients.push(...ingredients);
    this.ingredientAdded.next(this.ingredients.slice());
  }
}
