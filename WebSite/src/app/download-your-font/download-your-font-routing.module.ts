import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DownloadYourFontComponent } from './download-your-font.component';

const routes: Routes = [
  { path: '', component: DownloadYourFontComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DownloadYourFontRoutingModule { }
