;; remove the help message
(advice-add 'help-window-display-message :around #'ignore)

(let ((symbol (intern (car argv))))
  (cond ((fboundp symbol)
	 (message (substring-no-properties (describe-function symbol))))

	((boundp symbol)
	 (message "Such function doesn't exist, but there is a variable with same name."))

	(t (message "No documentation."))))
