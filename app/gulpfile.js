var gulp = require('gulp');
var browserSync = require('browser-sync');
var reload = browserSync.reload;


gulp.task('default', ['browser-sync']);

gulp.task('browser-sync', function () {
  browserSync({
    notify: false,
    server: {
      baseDir: "../htdocs"
    }
  });

  gulp.watch('htdocs/index.html', reload);

});
