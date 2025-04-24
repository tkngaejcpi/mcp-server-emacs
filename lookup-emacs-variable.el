;; remove the help message
(advice-add 'help-window-display-message :around #'ignore)

(let ((symbol (intern (car argv))))
  (cond ((boundp symbol)
	 (message (substring-no-properties (describe-variable symbol))))

	((fboundp symbol)
	 (message "Such variable doesn't exist, but there is a function with same name."))

	(t (message "No documentation."))))
