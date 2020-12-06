import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DownloadYourFontRoutingModule } from './download-your-font-routing.module';
import { DownloadYourFontComponent } from './download-your-font.component';
import { SharedModule } from '../shared/shared.module';


@NgModule({
  declarations: [DownloadYourFontComponent],
  imports: [
    CommonModule,
    DownloadYourFontRoutingModule,
    SharedModule
  ]
})
export class DownloadYourFontModule { }
