import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'themeColor',
})
export class ThemeColorPipe implements PipeTransform {

  private backgroundStyleMap: { [key: string]: string } = {
    'transparent': 'unset',
    'primary': 'var(--color-primary-default)',
    'success': 'var(--color-success-default)',
    'warning': 'var(--color-warning-default)',
    'danger': 'var(--color-danger-default)',
    'info': 'var(--color-info-default)',
    'alternate': 'var(--background-alternative-color-1)',
    'disabled': 'var(--bg-disabled-color)',
    'hint': 'var(--bg-hint-color)',
    'default': 'var(--background-basic-color-1)',
  };
  
  private textColors: { [key: string]: string } = {
    'basic': 'var(--text-basic-color)',
    'primary': 'var(--text-primary-color)',
    'success': 'var(--text-success-color)',
    'warning': 'var(--text-warning-color)',
    'danger': 'var(--text-danger-color)',
    'info': 'var(--text-info-color)',
    'alternate': 'var(--text-alternate-color)',
    'disabled': 'var(--text-disabled-color)',
    'hint': 'var(--text-hint-color)',
    'white': '#ffffff',
  };
  
  private textHoverColors: { [key: string]: string } = {
    'basic': 'var(--text-basic-color)',
    'primary': 'var(--text-primary-hover-color)',
    'success': 'var(--text-success-hover-color)',
    'warning': 'var(--text-warning-hover-color)',
    'danger': 'var(--text-danger-hover-color)',
    'info': 'var(--text-info-hover-color)',
    'alternate': 'var(--text-alternate-color)',
    'disabled': 'var(--text-disabled-color)',
    'hint': 'var(--text-hint-color)',
  };
  
  private textFocusColors: { [key: string]: string } = {
    'basic': 'var(--text-basic-color)',
    'primary': 'var(--text-primary-focus-color)',
    'success': 'var(--text-success-focus-color)',
    'warning': 'var(--text-warning-focus-color)',
    'danger': 'var(--text-danger-focus-color)',
    'info': 'var(--text-info-focus-color)',
    'alternate': 'var(--text-alternate-color)',
    'disabled': 'var(--text-disabled-color)',
    'hint': 'var(--text-hint-color)',
  };
  
  private cardStatusMap: { [key: string]: string } = {
    'default': 'var(--card-background-color)',
    'primary': 'var(--card-header-primary-background-color)',
    'success': 'var(--card-header-success-background-color)',
    'warning': 'var(--card-header-warning-background-color)',
    'danger': 'var(--card-header-danger-background-color)',
    'info': 'var(--card-header-info-background-color)',
  };

  transform(color: string, type?: string): string {
    if (type === 'background') {
      return this.backgroundStyleMap[color] || color;
    } else if (type === 'text') {
        return this.textColors[color];
    } else if (type === 'textHover') {
        return this.textHoverColors[color];
    } else if (type === 'textFocus') {
        return this.textFocusColors[color];
    } else if (type === 'cardStatus') {
        return this.cardStatusMap[color];
    }
    return color;
  }
}