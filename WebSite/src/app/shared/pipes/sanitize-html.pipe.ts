import { Pipe, PipeTransform } from '@angular/core';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
import { sanitize } from 'dompurify';

@Pipe({
  name: 'sanitizeHtml',
})
export class SanitizeHtmlPipe implements PipeTransform {
  constructor(private sanitizer: DomSanitizer) {}

  transform(unsafeHtml: string): SafeHtml {
    const saveHtml = sanitize(unsafeHtml, { ALLOW_UNKNOWN_PROTOCOLS: true });
    return this.sanitizer.bypassSecurityTrustHtml(saveHtml);
  }
}