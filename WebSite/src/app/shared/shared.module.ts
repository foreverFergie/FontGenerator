import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ThemeColorPipe } from './pipes/theme-color.pipe';
import { SanitizeHtmlPipe } from './pipes/sanitize-html.pipe';
import { NbListModule, NbButtonModule, NbIconModule } from '@nebular/theme';



@NgModule({
  declarations: [ThemeColorPipe, SanitizeHtmlPipe],
  imports: [
    CommonModule,
    NbListModule,
    NbButtonModule,
    NbIconModule
  ],
  exports: [ThemeColorPipe, SanitizeHtmlPipe, NbListModule, NbButtonModule, NbIconModule]
})
export class SharedModule { }
