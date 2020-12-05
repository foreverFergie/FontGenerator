import { NgModule } from '@angular/core';

import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
  { path: 'About', loadChildren: () => import('./upload-your-designs/upload-your-designs.module').then(m => m.UploadYourDesignsModule) },
  { path: 'Download-Your-Font', loadChildren: () => import('./download-your-font/download-your-font.module').then(m => m.DownloadYourFontModule) },
  { path: '', redirectTo: 'home', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule { }
