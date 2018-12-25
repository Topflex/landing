"use strict";

const {series, src, dest, watch} = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var cleanCSS = require('gulp-clean-css');

function style(cb) {
  return src('sass/style.scss')
  .pipe(sass())
  .pipe(autoprefixer({
    browsers: ['last 2 versions'],
    cascade: false
  }))
  .pipe(cleanCSS({compatibility: 'ie11'}))
  .pipe(dest('css'))
}

const monitor = function (cb) {
  watch(['sass/**/*.scss'], style);
} 


exports.default = monitor;