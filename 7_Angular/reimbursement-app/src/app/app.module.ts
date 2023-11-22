import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { FormComponent } from './form-component/form-component.component';
import { DataComponent } from './data/data.component';
import { FormService } from './app.service';

@NgModule({
  declarations: [AppComponent, FormComponent, DataComponent],
  imports: [BrowserModule, FormsModule],
  providers: [FormService],
  bootstrap: [AppComponent],
})
export class AppModule {}
