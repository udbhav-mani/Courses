import { Component, EventEmitter, Output } from '@angular/core';
import { Recipe } from '../recipe.model';
import { RecipeService } from '../recipes.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css'],
})
export class RecipeListComponent {
  constructor(
    private recService: RecipeService,
    private router: Router,
    private route: ActivatedRoute
  ) {}

  recipes: Recipe[];
  ngOnInit() {
    this.recipes = this.recService.getRecipe();
  }
  onNewRecipe() {
    this.router.navigate(['new'], { relativeTo: this.route });
  }
}
