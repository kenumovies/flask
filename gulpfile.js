'use strict';

// requirements

var gulp = require('gulp'),
    browserify = require('gulp-browserify'),
    size = require('gulp-size'),
    clean = require('gulp-clean'),
    sass = require('gulp-sass'),
    shell = require('gulp-shell');


// tasks

gulp.task('transform', function () {
  return gulp.src('./project/static/scripts/jsx/main.js')
    .pipe(browserify({transform: ['reactify']}))
    .pipe(gulp.dest('./project/static/scripts/js'))
    .pipe(size());
});

gulp.task('clean', function () {
  return gulp.src(['./project/static/scripts/js'], {read: false})
    .pipe(clean());
});

gulp.task('sass', function () {
  gulp.src('./project/static/sass/**/*.scss')
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(gulp.dest('./project/static/css'));
});

gulp.task('flask', shell.task(['python project/app.py']));

gulp.task('default', ['clean','sass'], function () {
  gulp.start('transform');
  gulp.watch('./project/static/scripts/jsx/main.js', ['transform']);
  gulp.watch('./project/static/sass/**/*.scss', ['sass']);
  gulp.start("flask")

});

