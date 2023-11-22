import { Component, EventEmitter, Input, Output } from '@angular/core';
import { RecipeService } from '../../recipes.service';

@Component({
  selector: 'app-recipe-item',
  templateUrl: './recipe-item.component.html',
  styleUrls: ['./recipe-item.component.css'],
})
export class RecipeItemComponent {
  @Input('recipe') recipe: any;
  @Input() index: any;

}
