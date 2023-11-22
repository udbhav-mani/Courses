import { Component } from '@angular/core';
import { Recipe } from '../recipe.model';
import { ShoppingListService } from 'src/app/shopping-list/shopping-list.service';
import { ActivatedRoute, Router } from '@angular/router';
import { RecipeService } from '../recipes.service';

@Component({
  selector: 'app-recipe-detail',
  templateUrl: './recipe-detail.component.html',
  styleUrls: ['./recipe-detail.component.css'],
})
export class RecipeDetailComponent {
  currentRecipe: Recipe = new Recipe('', '', '', []);
  id: number;
  constructor(
    private recipeService: RecipeService,
    private shopList: ShoppingListService,
    private route: ActivatedRoute,
    private router: Router
  ) {}
  ngOnInit() {
    this.route.params.subscribe((params) => {
      this.id = +params['id'];
      this.currentRecipe = this.recipeService.getRecipeById(this.id);
    });
  }
  addToList() {
    this.shopList.addIngredients(this.currentRecipe.ingredients);
  }
  editRecipe() {
    this.router.navigate(['edit'], { relativeTo: this.route });
  }
}
