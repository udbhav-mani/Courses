import {
  Directive,
  ElementRef,
  Renderer2,
  HostListener,
  HostBinding,
  Input,
} from '@angular/core';

@Directive({
  selector: '[highlightDirective]',
})
export class HighlightDirective {
  @Input('defaultColor') defaultColor: string = 'white';
  @Input('highlightColor') highlightColor: string = 'blue';
  @HostBinding('style.color') bgColor: string = this.defaultColor;

  constructor(private elRef: ElementRef, private renderer: Renderer2) {}
  ngOnInit() {
    this.elRef.nativeElement.style = 'background:red;'; // through direct
    this.renderer.setStyle(this.elRef.nativeElement, 'background', 'red'); // through renderer
  }
  // listens to event on host
  @HostListener('mouseenter') mouseOver() {
    // this.renderer.setStyle(this.elRef.nativeElement, 'color', 'blue'); // through renderer
    this.bgColor = this.highlightColor;
  }
  @HostListener('mouseleave') mouseLeave() {
    this.bgColor = this.defaultColor; // through renderer
  }
}
