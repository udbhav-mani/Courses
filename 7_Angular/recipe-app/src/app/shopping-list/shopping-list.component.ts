import { Component } from '@angular/core';
import { Ingredient } from '../shared/ingredient.model';
import { ShoppingListService } from './shopping-list.service';

@Component({
  selector: 'app-shopping-list',
  templateUrl: './shopping-list.component.html',
  styleUrls: ['./shopping-list.component.css'],
  providers: [],
})
export class ShoppingListComponent {
  constructor(private shopService: ShoppingListService) {}
  ingredients: Ingredient[];
  ngOnInit() {
    this.ingredients = this.shopService.getIngredients();
    this.shopService.ingredientAdded.subscribe((ingredients) => {
      this.ingredients = ingredients;
    });
  }
  addIngredientToList(ingredient: Ingredient) {
    this.shopService.addIngredient(ingredient);
  }
}
