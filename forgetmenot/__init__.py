#!/usr/bin/env python

from optparse import OptionParser
import sys

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

def run_text_quiz(quiz, options):
    import forgetmenot.text
    forgetmenot.text.run_quiz(quiz, options.strict)

def run_gui_quiz(quiz, options):
    try:
        import forgetmenot.gui
        forgetmenot.gui.run_quiz(quiz, options.font_size)
    except ImportError, e:
        if 'gtk' in e.args[0]:
            sys.stderr.write('error: pygtk not found. Install pygtk '
                             'or rerun with --text-mode.\n')
    except KeyboardInterrupt:
        pass

def main():
    options, args = get_options()
    quiz = load_quiz(args[0], options.reverse)

    if options.text:
        run_text_quiz(quiz, options)
    else:
        run_gui_quiz(quiz, options)

if __name__ == '__main__':
    main()
