#!/usr/bin/env python

from optparse import OptionParser

from forgetmenot.quiz import load_quiz

def get_options():
    parser = OptionParser(usage='%prog [OPTIONS] QUIZ',
                          version='%prog $Rev: 683 $')
    parser.add_option('-r', '--reverse', action='store_true',
                      dest='reverse', help=u'Reverse the deck.')
    parser.add_option('-t', '--text-mode', action='store_true',
                      dest='text', help=u'Force text mode.')
    parser.add_option('-s', '--strict', action='store_true',
                      dest='strict', help=u'Enable strict mode '
                      u'(require all possible definitions to be '
                      u'entered). Implies --text.')
    parser.add_option('--font-size', type='int', default=24,
                      dest='font_size', help='Font size to display '
                      u'quiz in.')

    options, args = parser.parse_args()

    if options.strict:
        options.text = True

    if len(args) != 1:
        parser.error(u'Required argument QUIZ missing.')

    return options, args

def main():
    options, args = get_options()
    quiz = load_quiz(args[0], options.reverse)

    if options.text:
        import forgetmenot.text
        run_quiz = forgetmenot.text.run_quiz
        args = [options.strict]
    else:
        import forgetmenot.gui
        run_quiz = forgetmenot.gui.run_quiz
        args = [options.font_size]

    try:
        run_quiz(quiz, *args)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
