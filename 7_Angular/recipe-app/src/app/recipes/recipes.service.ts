import { Recipe } from './recipe.model';
import { Ingredient } from '../shared/ingredient.model';
import { Subject } from 'rxjs';

export class RecipeService {
  private recipes = [
    new Recipe(
      'Recipe 1',
      'Vada Paao',
      'https://images.immediate.co.uk/production/volatile/sites/30/2020/08/chorizo-mozarella-gnocchi-bake-cropped-9ab73a3.jpg?quality=90&webp=true&resize=375,341',
      [
        new Ingredient('Paao', 2),
        new Ingredient('Potato', 1),
        new Ingredient('Spices', 1),
      ]
    ),
    new Recipe(
      'Pizza',
      'This is a test recipe',
      'https://images.unsplash.com/photo-1593560704563-f176a2eb61db?auto=format&fit=crop&q=80&w=1935&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
      [
        new Ingredient('All purpose flour', 1),
        new Ingredient('Oregano', 1),
        new Ingredient('Cheese', 1),
      ]
    ),
    new Recipe(
      'Pasta',
      'This is a test recipe',
      'https://images.unsplash.com/photo-1505253758473-96b7015fcd40?auto=format&fit=crop&q=80&w=1900&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
      [
        new Ingredient('All purpose flour', 1),
        new Ingredient('Oregano', 1),
        new Ingredient('Pasta', 2),
      ]
    ),
  ];
  getRecipe() {
    return this.recipes.slice();
  }
  getRecipeById(id: number) {
    return this.recipes[id];
  }
}
