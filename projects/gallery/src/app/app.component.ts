import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { ButtonComponent, TextBoxComponent, PasswordBoxComponent, LabelComponent } from 'angular'; // adjust import based on your build

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, ButtonComponent, TextBoxComponent, PasswordBoxComponent, LabelComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'gallery';
}
