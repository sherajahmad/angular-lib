import { Component, EventEmitter, Output } from "@angular/core";

@Component({
    selector: 'ui-button',
    standalone: true,
    inputs: ['text'],
    outputs: ['clicked'],
    template: `<button (click)="clicked.emit()">{{ text }}</button>`
  })
  export class UiButtonComponent {
    @Output() clicked = new EventEmitter<void>();
  }
  