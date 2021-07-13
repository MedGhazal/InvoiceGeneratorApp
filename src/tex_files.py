tex_template_la_mome = r"""\documentclass{letter}
\usepackage[french]{babel}
\usepackage[T1]{fontenc}
\usepackage{float}
\usepackage{invoice}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{geometry}
\usepackage{blindtext}
\usepackage{marvosym}
\pagestyle{fancy}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\fancypagestyle{plain}{
\lhead{\includegraphics[width=0.45\textwidth]{logo.png}
\begin{flushleft}
\begin{minipage}[t]{0.45\textwidth}
   Adressé à:\\ ADDRESS
\end{minipage}
\end{flushleft}
}
\rhead{
\begin{flushright}
\begin{minipage}[t]{0.35\textwidth}
    Date de facturation: DATEF\\DATEE
    Réf.: \textbf{FA}YEAR - COUNTER
\end{minipage}
\end{flushright}
\vspace{1cm}
\begin{flushright}
\begin{minipage}[t]{0.45\textwidth}
    Èmetteur:\\\textbf{\textsc{LA MOME Business SARLau}}\\
    QI \textsc{Sidi Ghanem} 158 1°étage bureau N°25\\ 
    Marrakech 40000\\
    \textbf{ICE}: 000113534000073
\end{minipage}
\end{flushright}}
\cfoot{
\footnotesize
\textbf{\textsc{LA MOME Business SARLau}}\\
\textit{QI \textsc{Sidi Ghanem} 158 1°étage bureau N°25 40000 Marrakech Morocco}\\
\textbf{ICE}: 000113534000073
\textbf{RC}: 68789 \\
\textbf{Patente}: 67194246
\textbf{IF}: 15257275 
\textbf{CNSS}: 4477495\\
\textbf{Téléphone}: 0662401636\\
}}
\pagestyle{plain}
\makeatletter
\let\ps@empty\ps@plain
\let\ps@firstpage\ps@plain
\makeatother
\address{}
\signature{}
\date{}
\begin{document}
\begin{letter}{}         
    \opening{}
    \vspace{1.5cm}
    \begin{invoice}{CURRENCY}{TVA}
    \ProjectTitle{\textsc{Facture}}	
	ACTIVITIES
    \end{invoice}   
    NOTE
    \vspace{.5cm}
    \textbf{Mode de paiement:} PAIMENTMODE\\
    \textbf{Banque:} Crédit du MAROC\\
    \textbf{SWIFT/BIC:} CDMAMAMC\\
    \textbf{IBAN:} MA21221450000010103007050233\\
  \end{letter}
\end{document}"""

tex_template_marina = r"""\documentclass{letter}
\usepackage[french]{babel}
\usepackage[T1]{fontenc}
\usepackage{float}
\usepackage{invoice}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{geometry}
\usepackage{blindtext}
\usepackage{marvosym}
\usepackage{geometry}
\geometry{top=4cm, bottom=4cm}
\pagestyle{fancy}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\fancypagestyle{plain}{
\rhead{
\begin{flushright}
\begin{minipage}[t]{0.35\textwidth}
    Date de facturation: DATEF\\DATEE
    Réf.: \textbf{FA}YEAR - COUNTER
\end{minipage}
\end{flushright}
\vspace{1cm}
\begin{flushright}
        \begin{minipage}[t]{0.45\textwidth}
            Èmetteur:\\\textbf{\textsc{VIDA Marina Yachting SRLAU}}\\
                        62 Lotissement Jnane 4 S.Y.B.A Marrakech 40000\\
                        \textbf{ICE}: 002241177000022
         \end{minipage}
\end{flushright}
}
\cfoot{
\footnotesize
\textbf{\textsc{VIDA Marina Yachting SRLAU}}\\
\textit{62 Lotissement Jnane 4 S.Y.B.A Marrakech 40000}\\
\textbf{Capital social}: 10 000 DHS
\textbf{ICE}: 002241177000022
\textbf{RC}: 96715 \\
\textbf{Patente}: 46300416 
\textbf{IF}: 37529690 
\textbf{CNSS}: 1501420\\
\textbf{Tel}: 06 67 08 58 98\\
}}
\pagestyle{plain}
\makeatletter
\let\ps@empty\ps@plain
\let\ps@firstpage\ps@plain
\makeatother
\address{}
\signature{}
\date{}
\begin{document}
  \begin{letter}{Adressé à:\\ ADDRESS}         
    \opening{}
    \begin{invoice}{CURRENCY}{TVA}
      \ProjectTitle{\textsc{Facture}}	
	ACTIVITIES
    \end{invoice}   
    NOTE
    \vspace{.5cm}
    \textbf{Mode de paiement:} PAIMENTMODE\\
    %\textbf{Banque:} Banque Populaire\\
    %\textbf{Numéro de compte principal:} 21211 3090636 000 8\\
  \end{letter}
\end{document}"""

tex_invoice = r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{invoice}[2018/08/06]
\newcount\invoice@language
\let\invoice@language=\language
\ifx\l@afrikaans\undefined	\newlanguage\l@afrikaans \fi
\ifx\l@dutch\undefined		\newlanguage\l@dutch \fi
\ifx\l@english\undefined	\newlanguage\l@english \fi
\ifx\l@estonian\undefined	\newlanguage\l@estonian \fi
\ifx\l@finnish\undefined	\newlanguage\l@finnish \fi
\ifx\l@french\undefined		\newlanguage\l@french \fi
\ifx\l@german\undefined		\newlanguage\l@german \fi
\ifx\l@italian\undefined	\newlanguage\l@italian \fi
\ifx\l@spanish\undefined	\newlanguage\l@spanish \fi
\ifx\l@swedish\undefined	\newlanguage\l@swedish \fi
\ifx\l@spanish\undefined	\newlanguage\l@spanish \fi
\ifx\l@spanishe\undefined	\newlanguage\l@spanishe \fi
\ifx\l@spanishv\undefined	\newlanguage\l@spanishv \fi

\DeclareOption{afrikaans}{\invoice@language=\number\l@afrikaans}
\DeclareOption{dutch}{\invoice@language=\number\l@dutch}
\DeclareOption{english}{\invoice@language=\number\l@english}
\DeclareOption{estonian}{\invoice@language=\number\l@estonian}
\DeclareOption{finnish}{\invoice@language=\number\l@finnish}
\DeclareOption{french}{\invoice@language=\number\l@french}
\DeclareOption{german}{\invoice@language=\number\l@german}
\DeclareOption{italian}{\invoice@language=\number\l@italian}
\DeclareOption{spanish}{\invoice@language=\number\l@spanish}
\DeclareOption{spanishe}{\invoice@language=\number\l@spanishe}
\DeclareOption{spanishv}{\invoice@language=\number\l@spanishv}
\DeclareOption{swedish}{\invoice@language=\number\l@swedish}
\DeclareOption{position}{}
\newif\ifcomma
\DeclareOption{comma}{\commatrue}
\ProcessOptions
\RequirePackage{ifthen}
\RequirePackage{longtable}
\RequirePackage{calc}
\ifcomma
	\RequirePackage[output-decimal-marker={,}]{siunitx}
\else
	\RequirePackage{siunitx}
\fi
\RequirePackage{fp}
\input{invoicelabels.sty}
%
\newcommand{\InvoiceVersion}{0.91}%
\newcounter{Fee}		%
\newcounter{VAT}		%
%\newcounter{VAT@rate}		%
\newcounter{Expenses}		%
\newcounter{Discount}		% Discount item
\newcounter{Total}		%
\newcounter{Project}		%
%
\newcounter{Fee@ctr}		% Number of fees per project
				% no subtotal will be printed in case of
				% value < 2
%
\newcounter{Expense@ctr}	% Number of expense items per project
				% no subtotal will be printed in case of
				% value < 2
%
\newcounter{One@Fee}		% Individual Fee
\newcounter{One@VAT}		% Individual VAT
\newcounter{One@Expense}	% Individual Expense
%
\newcounter{ST@Fee}		% Subtotal Fee
\newcounter{ST@VAT}		% Subtotal VAT
\newcounter{ST@Expenses}	% Subtotal Expenses
\newcounter{ST@Project}		% Subtotal Project
%
\gdef\Flag{0}%			% State 0: Invoice not started yet
				% State 1: Start invoice
				% State 2: Start project, print title
				% State 3: Fee Item
				% State 4: Print Subtotal Fee
				% State 5: Expense Item
				% State 6: Print Subtotal Expenses
				% State 7: Print Subtotal Project
				% State 8: Print Total, Close invoice
%
\gdef\Project{}%		% Empty Project Name
\def\Null{0}%
\newif\ifVATnonzero
% \def\BC{Euro}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%\newcommand{\my@message}[1]{\message{^^J#1^^J^^J}}
\newcommand{\error@message}[1]{\errmessage{^^J\Error: #1^^J^^J}}
\newcommand{\warning@message}[1]{\message{^^J\Warning: #1^^J^^J}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifx\invoice\undefined			% False if KOMA Script scrlettr.cls
	\def\my@invoice{invoice}	% loaded. In this case one may say
\else					% "invoice". If true, the environ-
	\def\my@invoice{invoiceenv}	% ment is renamed to "invoiceenv"
	\let\invoiceno\invoice		% and the scrlettr macro is renamed
	\def\invoice#1{%		% to "invoiceno". Thank you, Thilo,
		\error@message{\KOMA}}	% for this hint!
\fi					%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newenvironment{\my@invoice}[2]{%
	\setcounter{Fee@ctr}{0}%		% reset counter
	\setcounter{Expense@ctr}{0}%		% reset counter
	\def\Null{0}%
	\setcounter{Project}{0}%
	\ST@Reset\Total@Reset%
	\def\BC{#1}%
	\def\VAT@rate{#2}%
	\ifx\VAT@rate\Null\VATnonzerofalse\else\VATnonzerotrue\fi%
	\ifVATnonzero
		\message{^^J^^JVAT is not zero!^^J^^J}%
	\else
		\message{^^J^^JVAT is zero!^^J^^J}%
	\fi%
	% The VAT is: \the\VAT@rate % Debugging Diagnostics only
	\parindent=0cm%
	\ifcase\Flag % 0: Invoice not started yet
		%
		\gdef\Flag{1}%
		%\begin{center}% Removed 20050621 by suggestion from ...
		\begin{longtable}{p{5cm}lrrr}%
		%
	\else \error@message{\NoInvoiceNesting}%
	\fi}%
% At the end of environment: 
% Yields state 8->0, Close and complete invoice, finish tables, etc.
{% 
	\ifcase\Flag % 0: Invoice not started yet
		%
		\error@message{\MissingOpening}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 1: Start invoice
		%
		\error@message{\MissingProject}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 2: Start project, print title
		%
		\error@message{\MissingInputData}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 3: Print remuneration item
		%
		\ifnum\theProject>0 \ST@Fee\ST@Project\fi%
		\Tot@l%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 4: Print subtotal remuneration
		%
		\ifnum\theProject>1 \ST@Project\fi%
		\Tot@l%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 5: Expense item
		%
		\ifnum\theProject>1 \ST@Expenses\ST@Project\fi%
		\Tot@l%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 6: Print subtotal expenses
		%
		\ifnum\theProject>1 \ST@Project\fi%
		\Tot@l%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 7: Print subtotal project
		%
		\Tot@l%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 8: Print total, close invoice
		%
		\warning@message{\InvoiceCompleted}%
		%
	\else \error@message{\InternalError}%
	\fi%
	\gdef\Flag{0}%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\ProjectTitle}[1]{% Yields state 2: Start Project
	%\gdef\NewProject{#1}
	%
	\ifcase\Flag% 0: Invoice not started yet
	%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or 	% 1: Start invoice
		%
		\Project@Title{#1}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 2: Start project, print title
		%
		\error@message{\NoProjectNesting}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 3: Print remuneration item
		%
		\ST@Fee%
		\ST@Project%
		\Project@Title{#1}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 4: Print subtotal remuneration
		%
		\ST@Project%
		\Project@Title{#1}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 5: Expense item
		%
		\ST@Expenses%
		\ST@Project%
		\Project@Title{#1}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 6: Print subtotal expenses
		%
		\ST@Project%
		\Project@Title{#1}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 7: Print subtotal project
		%
		\Project@Title{#1}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 8: Print total, close invoice
		%
		\error@message{\InvoiceCompletedNoProject}%
		%
	\else \error@message{\InternalError}%
	\fi%
	\setcounter{Fee@ctr}{0}%		% reset counter
	\setcounter{Expense@ctr}{0}%		% reset counter
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Fee}[3]{% Yields state 3, Print Fee Item
	%
	% #1 Contents
	% #2 Fee per Unit
	% #3 Unit Count
	%
	\ifcase\Flag % 0: Invoice not started yet
		\error@message{\MissingOpening}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 1: Start invoice
		%
		\error@message{\MissingProject}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 2: Start project, print title
		%
		\Fee@Title%
		\Fee@Line{#1}{#2}{#3}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 3: Print remuneration item
		%
		\Fee@Line{#1}{#2}{#3}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 4: Print subtotal remuneration
		%
		\warning@message{\FeeSTExists}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 5: Expense item
		%
		\error@message{\FeeBeforeExpense}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 6: Print subtotal expenses
		%
		\error@message{\FeeBeforeExpense}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 7: Print subtotal project
		%
		\error@message{\ProjectCompletedNoFee}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 8: Print total, close invoice
		%
		\error@message{\InvoiceCompletedNoFee}%
		%
		%
	\else \error@message{\InternalError}%
	\fi%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\STFee}{% Yields state 4, print subtotal remuneration
	%
	\ifcase\Flag % 0: Invoice not started yet
		%
		\error@message{\MissingOpening}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 1: Start invoice
		%
		\error@message{\MissingProject}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 2: Start project, print title
		%
		\error@message{\MissingFee}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 3: Print remuneration item
		%
		\Print@ST@Fees%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 4: Print subtotal remuneration
		%
		\warning@message{\FeeSTExists}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 5: Expense item
		%
		\error@message{\FeeBeforeExpense}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 6: Print subtotal expenses
		%
		\error@message{\FeeBeforeExpense}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 7: Print subtotal project
		%
		\error@message{\ProjectCompletedNoFee}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 8: Print total, close invoice
		%
		\error@message{\ProjectCompletedNoFee}%
		%
	\else \error@message{\InternalError}%
	\fi%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\EBC}[2]{% Yields state 5: Expenses in BaseCurrency 
	%
	% #1 Contents und Datum
	% #2 Amount in BaseCurrency
	%
	\ifcase\Flag % 0: Invoice not started yet
		%
		\error@message{\MissingOpening}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 1: Start invoice
		%
		\error@message{\MissingProject}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 2: Start project, print title
		%
		\Expense@Title%
		\Expense@BaseCurrency{#1}{#2}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 3: Print remuneration item
		%
		\ST@Fee%
		\Expense@Title%
		\Expense@BaseCurrency{#1}{#2}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 4: Print subtotal remuneration
		%
		\Expense@Title%
		\Expense@BaseCurrency{#1}{#2}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 5: Expense item
		%   
		\Expense@BaseCurrency{#1}{#2}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 6: Print subtotal expenses
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 7: Print subtotal project
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 8: Print total, close invoice
		%
		\error@message{\InvoiceCompletedNoExpense}%
		%
	\else \error@message{\InternalError}%
	\fi%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\EBCi}[2]{% Yields state 5: Expenses in BaseCurrency 
	%				But, unlike base form (no
	%				'invisible') this version does
	%				not state the item, it only
	%				the total amount of expenses. 
	%
	% #1 Contents und Datum
	% #2 Amount in BaseCurrency
	%
	\ifcase\Flag % 0: Invoice not started yet
		%
		\error@message{\MissingOpening}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 1: Start invoice
		%
		\error@message{\MissingProject}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 2: Start project, print title
		%
		%\Expense@Title%
		\Expense@Base@Currency{#1}{#2}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 3: Print remuneration item
		%
		\ST@Fee%
		%\Expense@Title%
		\Expense@Base@Currency{#1}{#2}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 4: Print subtotal remuneration
		%
		%\Expense@Title%
		\Expense@Base@Currency{#1}{#2}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 5: Expense item
		%   
		\Expense@Base@Currency{#1}{#2}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 6: Print subtotal expenses
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 7: Print subtotal project
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 8: Print total, close invoice
		%
		\error@message{\InvoiceCompletedNoExpense}%
		%
	\else \error@message{\InternalError}%
	\fi%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\EFC}[5]{% Yields state 5: Expenses in ForeignCurrency
	%
	% #1 Contents und Datum
	% #2 Currency
	% #3 Amount
	% #4 Exchange Rate
	% #5 Amount Zielwaehrung
	%
	% Usage:
	% 1. {Contents}{ForeignCurrency}{ExchangeRate}{}
	% 2. {Contents}{ForeignCurrency}{}{BaseCurrency}
	% 3. {Contents}{ForeignCurrency}{ExchangeRate}{BaseCurrency}
	%
	\ifcase\Flag % 0: Invoice not started yet
		%
		\error@message{\MissingOpening}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 1: Start invoice
		%
		\error@message{\MissingProject}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 2: Start project, print title
		%
		\Expense@Title%
		\Expense@ForeignCurrency{#1}{#2}{#3}{#4}{#5}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 3: Print remuneration item
		%
		\ST@Fee%
		\Expense@Title%
		\Expense@ForeignCurrency{#1}{#2}{#3}{#4}{#5}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 4: Print subtotal remuneration
		%
		\Expense@Title%
		\Expense@ForeignCurrency{#1}{#2}{#3}{#4}{#5}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 5: Expense item
		%
		\Expense@ForeignCurrency{#1}{#2}{#3}{#4}{#5}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 6: Print subtotal expenses
		%
		\error@message{\ProjectCompletedNoExpense}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 7: Print subtotal project
		%
		\error@message{\ProjectCompletedNoExpense}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 8: Print total, close invoice
		%
		\error@message{\InvoiceCompletedNoExpense}%
		%
	\else \error@message{\InternalError}%
	\fi%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\EFCi}[5]{% Yields state 5: Expenses in ForeignCurrency
	%				But, unlike base form (no
	%				'invisible') this version does
	%				not state the item, it only
	%				the total amount of expenses. 
	%
	% #1 Contents und Datum
	% #2 Currency
	% #3 Amount
	% #4 Exchange Rate
	% #5 Amount Zielwaehrung
	%
	% Usage:
	% 1. {Contents}{ForeignCurrency}{ExchangeRate}{}
	% 2. {Contents}{ForeignCurrency}{}{BaseCurrency}
	% 3. {Contents}{ForeignCurrency}{ExchangeRate}{BaseCurrency}
	%
	\ifcase\Flag % 0: Invoice not started yet
		%
		\error@message{\MissingOpening}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 1: Start invoice
		%
		\error@message{\MissingProject}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 2: Start project, print title
		%
		\Expense@Title%
		\Expense@Foreign@Currency{#1}{#2}{#3}{#4}{#5}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 3: Print remuneration item
		%
		\ST@Fee%
		% \Expense@Title%
		\Expense@Foreign@Currency{#1}{#2}{#3}{#4}{#5}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 4: Print subtotal remuneration
		%
		% \Expense@Title%
		\Expense@Foreign@Currency{#1}{#2}{#3}{#4}{#5}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 5: Expense item
		%
		\Expense@Foreign@Currency{#1}{#2}{#3}{#4}{#5}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 6: Print subtotal expenses
		%
		\error@message{\ProjectCompletedNoExpense}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 7: Print subtotal project
		%
		\error@message{\ProjectCompletedNoExpense}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 8: Print total, close invoice
		%
		\error@message{\InvoiceCompletedNoExpense}%
		%
	\else \error@message{\InternalError}%
	\fi%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\STExpenses}{% Yields state 6: Ausgabe der ST Expenses
	%
	\ifcase\Flag % 0: Invoice not started yet
		%
		\error@message{\MissingOpening}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 1: Start invoice
		%
		\error@message{\MissingProject}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		%
	\or	% 2: Start project, print title
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		%
	\or	% 3: Print remuneration item
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		%
	\or	% 4: Print subtotal remuneration
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 5: Expense item
		%
		\Print@ST@Expenses%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 6: Print subtotal expenses
		%
		\warning@message{\ProjectCompletedNoExpense}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 7: Print subtotal project
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 8: Print total, close invoice
		%
		\error@message{\InvoiceCompletedNoExpense}%
		%
	\else \error@message{\InternalError}%
	\fi%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\STProject}{% Yields state 7: Ausgabe der ST Project
	%
	\ifcase\Flag % 0: Invoice not started yet
		%
		\error@message{\MissingOpening}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 1: Start invoice
		%
		\error@message{\MissingProject}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 2: Start project, print title
		%
		\warning@message{\ProjectEmpty}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 3: Print remuneration item
		%
		\ST@Fee%
		\ST@Project%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 4: Print subtotal remuneration
		%
		\ST@Project%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 5: Expense item
		%
		\ST@Expenses%
		\ST@Project%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 6: Print subtotal expenses
		%
		\ST@Project%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 7: Print subtotal project
		%
		\warning@message{\ProjectSTExists}%
		%
	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\or	% 8: Print total, close invoice
		%
		\error@message{\InvoiceCompletedNoProjectST}%
		%
	\else \error@message{\InternalError}%
	\fi%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Discount}[2]{%	Yields no particular state.
	%			Inserts discount in project total,
	%			names discount reason
	%			and amount of discount
	%
	\gdef\Discount@Contents{#1}%
	\setcounter{Discount}{100 * \real{-#2}}%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Total@Reset}{%
	\setcounter{Fee}{0}%
	\setcounter{VAT}{0}%
	\setcounter{Expenses}{0}%
	\setcounter{Total}{0}%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\ST@Reset}{%
	\setcounter{ST@Fee}{0}%
	\setcounter{ST@VAT}{0}%
	\setcounter{ST@Expenses}{0}%
	\setcounter{ST@Project}{0}%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Print@Value}[1]{%
	\FPmul\r#1{0.01}%% <- Reduce to BaseCurrency
	\FPtrunc\r\r{2}%% <- Truncate to two digits
	\num{\r}%		% <- Output data!
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Message@Value}[1]{%
	\FPmul\r#1{0.01}%% <- Reduce to BaseCurrency
	\FPtrunc\r\r{2}%% <- Truncate to two digits
	\message{\r}%	% <- Output data!
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Project@Title}[1]{%
	% Internal command called by \ProjectTitle.
	%
	\gdef\Flag{2}%
	\gdef\Project{#1}%
	\ST@Reset\addtocounter{Project}{1}%
	\ifnum\theProject>1 \\\\\else\\\fi%
	\multicolumn{5}{c}{\textbf{\large#1}}\\%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Fee@Title}{%
	\\
	\noindent\textbf{\Activity}&&\UnitRate&&\Amount\ (\BC)\\
	\hline%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Fee@Line}[3]{%
	%
	% #1 Contents
	% #2 Charged Fee per Unit
	% #3 Count
	%
	% Internal command, called by \Fee.
	%
	\gdef\Flag{3}%
	%
	#1			&	&#2	&&
%
%   next is reversed to allow real arithmetic.
%   intermediate results are stored in integer format,
%   so calculations are incorrect in case #2 is a real.
%   fixed by exchanging the 1 and the 100
%
		\FPmul\r{100}{#2}% added 2006-01-04
		\setcounter{One@Fee}{1 *\real{\r} * \real{#3} }%
%
		\addtocounter{ST@Fee}{\theOne@Fee}%
		\addtocounter{Fee}{\theOne@Fee}%
		\addtocounter{Fee@ctr}{1}%	    increase counter with 1
		\Print@Value{\theOne@Fee}\\%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\ST@Fee}{%
	% \gdef\Flag{4}%
	\ifnum\theST@Fee>0%
	    \ifthenelse{\theFee@ctr>1} %	    % if more than 1 \Fee line
		{\Print@ST@Fees%					% print it, else
		}%
	    {}%									% do nothing
		\ifVATnonzero\ST@VAT@Printout\fi%
	\fi%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Print@ST@Fees}{%
	\gdef\Flag{4}%
	\SubtotalFee &	&	&	&%	print the subtotal of fees
		\Print@Value{\theST@Fee}\\%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\ST@VAT@Printout}{%
		\VAT\ (\VAT@rate\%)	 &	&	&	&%
		\FPset\x{\VAT@rate}
		\FPset\res{\theST@Fee}
		\FPadd\x{\x}{100}
		\FPdiv\res{\res}{\x}
		\FPmul\res{\res}{100}
		\FPeval\res{round(res:0)}
		\FPsub\res{\theST@Fee}{\res}
		\setcounter{ST@VAT}{1*\real{\res}}%
			%\setcounter{ST@VAT}{\theST@Fee - \theST@Fee / (\real{\VAT@rate} / 100 + 1)}%
				\Print@Value{\theST@VAT}\\%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Expense@BaseCurrency}[2]{%
	#1			& \BC		&	&	&%
	\gdef\Flag{5}%
	\FPmul\r{100}{#2}%
	\setcounter{One@Expense}{1*\real{\r}}%
	\addtocounter{ST@Expenses}{\theOne@Expense}%
	\addtocounter{Expenses}{\theOne@Expense}%
	\addtocounter{Expense@ctr}{1}%advance counter
				\Print@Value{\theOne@Expense}\\%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Expense@Base@Currency}[2]{%
	\gdef\Flag{5}%
	\FPmul\r{100}{#2}%
	\setcounter{One@Expense}{1*\real{\r}}%
	\addtocounter{ST@Expenses}{\theOne@Expense}%
	\addtocounter{Expenses}{\theOne@Expense}%
	\addtocounter{Expense@ctr}{1}%advance counter
		&	&	&	&	\\[-1.2em]% This is an ugly kludge:
								  %	Inserting an empty line
								  % which rolls backwards
								  % makes disappear the spurious
								  % spaces caused by external
								  % routines.
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Expense@ForeignCurrency}[5]{%
	\gdef\Flag{5}%
	%
	% Folgende Angaben sind moeglich:
	% 1. {Contents}{Currency}{Amount}{Umrechnung}{  }
	% 2. {Contents}{Currency}{Amount}{          }{BaseCurrency}
	% 3. {Contents}{Currency}{Amount}{Umrechnung}{BaseCurrency}
	%
	#1	 & #2	& #3	& #4&%
	\ifthenelse{\equal{#5}{}}% Target in BaseCurrency or not?
		{% Target not in BaseCurrency
			\FPmul\r{100}{#3}%
			\FPmul\r \r {#4}%
		}%
		{% Target in BaseCurrency
			\FPmul\r{100}{#5}%
		}%
	\setcounter{One@Expense}{1*\real{\r}}%
	\addtocounter{ST@Expenses}{\theOne@Expense}%
	\addtocounter{Expenses}{\theOne@Expense}%
	\addtocounter{Expense@ctr}{1}%advance counter
	\Print@Value{\theOne@Expense}%
\\%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Expense@Foreign@Currency}[5]{%
	\gdef\Flag{5}%
	%
	% Folgende Angaben sind moeglich:
	% 1. {Contents}{Currency}{Amount}{Umrechnung}{  }
	% 2. {Contents}{Currency}{Amount}{          }{BaseCurrency}
	% 3. {Contents}{Currency}{Amount}{Umrechnung}{BaseCurrency}
	%
	\ifthenelse{\equal{#5}{}}% Target in BaseCurrency or not?
		{% Target not in BaseCurrency
			\FPmul\r{100}{#3}%
			\FPmul\r\r{#4}%
		}%
		{% Target in BaseCurrency
			\FPmul\r{100}{#5}%
		}%
	\setcounter{One@Expense}{1*\real{\r}}%
	\addtocounter{ST@Expenses}{\theOne@Expense}%
	\addtocounter{Expenses}{\theOne@Expense}%
	\addtocounter{Expense@ctr}{1}%advance counter
		&	&	&	&	\\[-1.2em]% ugly kludge as above
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Expense@Title}{%
	\\%
	\textbf{\Expense}&\Currency&\Amount&\Factor &\BC\\%
	\hline%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\ST@Expenses}{%
	% \gdef\Flag{6}%
	\ifnum\theST@Expenses>0%
	    \ifthenelse{\theExpense@ctr>1}%	    % if more than 1 Expense line
		{\Print@ST@Expenses}%				% print it, else
		{}%									% do nothing
	\fi%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Print@ST@Expenses}{%
	\gdef\Flag{6}%
		&	&	&	&	\\[-1.2em]% ugly kludge as above
	\SubtotalExpenses &	&	&	&%	print the subtotal of expenses
		\Print@Value{\theST@Expenses}\\%
}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\ST@Project}{%
	\gdef\Flag{7}%
	\\
	%\multicolumn{4}{l}{\SubtotalProject}%
	%\let\Project\NewProject%
	%&
	\SubtotalProject &	&	&	& 
			\FPset\x{\VAT@rate}
			\FPset\res{\theST@Fee}
			\FPadd\x{\x}{100}
			\FPdiv\res{\res}{\x}
			\FPmul\res{\res}{100}
			\FPeval\res{round(res:0)}
			%\FPsub\res{\theST@Fee}{\res}
			\setcounter{ST@Fee}{1*\real{\res}}%
			\addtocounter{ST@Project}{\theST@Fee}
			\addtocounter{ST@Project}{\theST@Expenses}
			\Print@Value{\theST@Project}\\
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\Total@VAT@Printout}{%
		\FPset\x{\VAT@rate}
		\FPset\y{\theFee}
		\FPset\z{100}
		\FPset\res{0}
		\FPdiv\myVAT{\x}{\z}
		\FPmul\res{\myVAT}{\y}
		\FPeval\res{round(res:2)}
		\setcounter{VAT}{1*\real{\res}}%
		\SumVAT	&	&	&	&\Print@Value{\theVAT}\\%
}%
\newcommand{\Tot@l}{%
	\hline\hline
	\textbf{\Total}&   &	&	&%
		\message{^^J\Currency: \BC}%
		\message{^^J\VAT: \VAT@rate}%
		\addtocounter{Total}{\theFee}%
		\message{^^J\SumFees: }\Message@Value{\theFee}%
		\addtocounter{Total}{\theVAT}%
		\message{^^J\SumVAT: }\Message@Value{\theVAT}%
		\addtocounter{Total}{\theExpenses}%
		\message{^^J\SumExpenses: }\Message@Value{\theExpenses}%
		\ifnum\theDiscount<0 %
		\addtocounter{Total}{\theDiscount}%
		\message{^^J\Discount@Contents: }\Message@Value{\theDiscount}%
		\fi %
		\textbf{\Print@Value{\theTotal}}%
		\message{^^J\Total: }%
			\Message@Value{\theTotal}\message{^^J^^J}\\%
	\end{longtable}
	%\end{center}% Removed 20050621 by suggestion from ...
	\gdef\Flag{8}%
}
\endinput
"""

tex_invoicelabels = r"""\def\InvoiceCompleted	{Invoice completed. Command ignored.}%
\def\FeeSTExists	{You cannot print a fee subtotal twice!}%
\def\ProjectEmpty	{Project empty. No subtotal possible!}%
\def\ProjectSTExists	{You cannot print a project subtotal twice!}%
\def\InternalError			{Package `invoice': Internal error!}%
%
\def\NoInvoiceNesting			{Invoices cannot be nested.
					 Close this invoice first!}%
%
\def\InvoiceCompletedNoExpense		{Invoice closed.
					 No new expense item allowed.
					 Start a new invoice
					 first!}%
%
\def\InvoiceCompletedNoFee		{Invoice closed.
					 No new fee item allowed.
					 Start a new invoice
					 first!}%
%
\def\InvoiceCompletedNoFeeST		{Invoice closed.
					 No fee subtotal allowed.
					 Start a new invoice
					 first!}%
%
\def\InvoiceCompletedNoProject		{Invoice closed.
					 No new project allowed.
					 Start a new invoice
					 first!}%
%
\def\InvoiceCompletedNoProjectST	{Invoice closed.
					 No project subtotal allowed.
					 Start a new invoice
					 first!}%
%
\def\MissingFee				{No fee given.
					 You must charge at least one fee!}%
%
\def\MissingInputData			{Missing input data!}%
%
\def\MissingOpening			{You must open an invoice!}%
%
\def\MissingProject			{No project given.
					 Open a project first!}%
%
\def\FeeBeforeExpense			{Fees are charged first.
					 Expenses follow.}%
%
\def\NoProjectNesting			{Projects cannot be nested.
					 Close this project first!}%
%
\def\ProjectCompletedNoExpense		{Project closed.
					 No new expense item allowed.
					 Start a new project
					 first!}%
%
\def\ProjectCompletedNoFee		{Project closed.
					 No new fee item allowed.
					 Start a new project
					 first!}%
%
\def\KOMA				{Users of KOMA-Script's scrlettr.cls%
					 ^^Jsay `invoiceno' for the scrlettr
					 invoice command,^^Jand `invoiceenv'
					 for the invoice environment!}%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Labels. These ones are available in translation, too. See below.
%
\def\Warning				{Warning}%
\def\Error				{Error}%
\def\Expense				{Expense}%
\def\Amount				{Amount}%
\def\Currency				{Currency}%
\def\Factor				{Factor}%
\def\Activity				{Activity}%
\def\Count				{Count}%
\def\UnitRate				{Rate/Unit}%
\def\Fees				{Fees}%
\def\VAT				{VAT}%
\def\Expenses				{Expenses}%
\def\SumFees				{Sum \Fees}%
\def\SumVAT				{Sum \VAT}%
\def\SumExpenses			{Sum \Expenses}%
\def\SubtotalFee			{Subtotal \Fees}%
\def\SubtotalExpenses			{Subtotal \Expenses}%
\def\SubtotalProject			{Subtotal \Project}%

\def\Total				{Total}%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Languages other than English in alphabetical order.
% So far we have:
% - Afrikaans
% - Czech
% - Dutch
% - (English) (default)
% - Estonian
% - Finnish
% - French
% - German
% - Italian
% - Spanish I
% - Spanish II, with strong English influences
% - Spanish III, a variant
% - Swedish
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is Afrikaans.
%
\ifx\l@afrikaans\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@afrikaans\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@afrikaans
	\def\Warning			{Waarskuwing}
	\def\Error			{Fout}
	\def\Expense			{Onkostes}
	\def\Amount			{Bedrag}
	\def\Currency			{Valuta}
	\def\Factor			{Faktor}
	\def\Activity			{Aktiwiteit}
	\def\Count			{Aantal ure}
	\def\UnitRate			{Tarief}
	\def\Fees			{Fooie}
	\def\VAT			{BTW}
	\def\Expenses			{Uitgawes}
	\def\SumFees			{Totaal Fooie}
	\def\SumVAT			{Totaal BTW}
	\def\SumExpenses		{Totaal Uitgawes}
	\def\SubtotalFee		{Subtotaal \Fees}
	\def\SubtotalExpenses		{Subtotaal \Expenses}
	\def\SubtotalProject		{Subtotaal \Project}
	\def\Total			{Totaal}
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is Czech.
%
\ifx\l@czech\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@czech\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@czech
	\def\Warning			{Upozorn{\v e}n{\' i}}%
	\def\Error			{Chyba}%
	\def\Expense			{VÃ½daj}%
	\def\Amount			{Cena}%
	\def\Currency			{M{\v e}na}%
	\def\Factor			{Pom{\e }r}%
	\def\Activity			{{\v C}innost}%
	\def\Count			{Po{\v c}et}%
	\def\UnitRate			{Cena}%
	\def\Fees			{Cena}%
	\def\VAT			{DPH}%
	\def\Expenses			{V{\' y}daje}%
	\def\SumFees			{\Fees celkem bez \VAT}%
	\def\SumVAT			{\VAT celkem}%
	\def\SumExpenses		{\Expenses celkem}%
	\def\SubtotalFee		{Mezisou{\v c}et \Fees}%
	\def\SubtotalExpenses		{Mezisou{\v c}et \Expenses}%
	\def\SubtotalProject		{Mezisou{\v c}et \Project}%
	\def\Total			{Celkem k {\' u}hrad{\v e}}%
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is Dutch.
%
\ifx\l@dutch\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@dutch\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@dutch
	\def\Warning			{Waarschuwing}%
	\def\Error			{Fout}%
	\def\Expense			{Onkosten}%
	\def\Amount			{Bedrag}%
	\def\Currency			{Valuta}%
	\def\Factor			{Faktor}%
	\def\Activity			{Activiteit}%
	\def\Count			{Aantal}%
	\def\UnitRate			{Prijs/Eenheid}%
	\def\Fees			{Honorarium}%
	\def\VAT			{BTW}%
	\def\Expenses			{Onkosten}%
	\def\SumFees			{Totaal \Fees}%
	\def\SumVAT			{Totaal \VAT}%
	\def\SumExpenses		{Totaal \Expenses}%
	\def\SubtotalFee		{Subtotaal \Fees}%
	\def\SubtotalExpenses		{Subtotaal \Expenses}%
	\def\SubtotalProject		{Subtotaal \Project}%
	\def\Total			{Totaal}%
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is Estonian
\ifx\l@estonian\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@estonian\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@estonian
  \def\Warning          {Hoiatus} %
  \def\Error            {Viga} %
  \def\Expense          {Kulu} %
  \def\Amount           {Kogus} %
  \def\Currency         {Valuuta} %
  \def\Factor           {Kordaja} %
  \def\Activity         {Tegevus} %
  \def\Count            {Arv} %
  \def\UnitRate         {\"{U}hiku hind} %
  \def\Fees             {Maksud} %
  \def\VAT              {K\"{a}ibemaks} %
  \def\Expenses         {Kulud} %
  \def\SumFees          {Maksude summa} %
  \def\SumVAT           {K\"{a}ibemaksu summa} %
  \def\SumExpenses      {Kulutuste summa} %
  \def\SubtotalFee      {Maksude vahesumma} %
  \def\SubtotalExpenses {Kulude vahesumma} %
  \def\SubtotalProject  {Projekti vahesumma} %
  \def\Total            {Kogusumma} %
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is Finnish
\ifx\l@finnish\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@finnish\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@finnish
	\def\Warning			{Varoitus} % Enter translations here!
	\def\Error			{Virhe} %
	\def\Expense			{Kulu} %
	\def\Amount			{Summa} %
	\def\Currency			{Valuutta} %
	\def\Factor			{Kerroin} %
	\def\Activity			{Laskutusperuste} %
	\def\Count			{MÃ¤Ã¤rÃ¤} %
	\def\UnitRate			{YksikkÃ¶hinta} %
	\def\Fees			{TyÃ¶t} %
	\def\VAT			{ALV} %
	\def\Expenses			{Kulut} %
	\def\SumFees			{TyÃ¶t yhteensÃ¤} %
	\def\SumVAT			{ALV yhteensÃ¤} %
	\def\SumExpenses		{Kulut yhteensÃ¤} %
	\def\SubtotalFee		{TyÃ¶t vÃ¤lisumma} %
	\def\SubtotalExpenses		{Kulut vÃ¤lisumma} %
	\def\SubtotalProject		{VÃ¤lisumma} %
	\def\Total			{YhteensÃ¤} %
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is French.
%
\ifx\l@french\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@french\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@french
	\def\Warning			{Avertissement}%
	\def\Error				{Erreur}%
	\def\Expense			{D\'epense}%
	\def\Amount				{Montant}%
	\def\Currency			{Devise}%
	\def\Factor				{Facteur}%
	\def\Activity			{Activit\'e}%
	\def\Count				{Quantit\'e}%
	\def\UnitRate			{Prix}%
	\def\Fees				{HT}%
	\def\VAT				{TVA}%
	\def\Expenses			{D\'epenses}%
	\def\SumFees			{sTotal HT}%
	\def\SumVAT				{sTotal TVA}%
	\def\SumExpenses		{sTotal TTC}%
	\def\SubtotalFee		{Total TTC}%
	\def\SubtotalExpenses	{Sous-Total \Expenses}%
	\def\SubtotalProject	{Total HT}%
	\def\Total				{Total \`{a} payer}%
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is German.
%
\ifx\l@german\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@german\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@german
	\def\Warning			{Warnung}%
	\def\Error			{Fehler}%
	\def\Expense			{Auslage}%
	\def\Amount			{Betrag}%
	\def\Currency			{W\"ahrung}%
	\def\Factor			{Faktor}%
	\def\Activity			{Aktivit\"at}%
	\def\Count			{Anzahl}%
	\def\UnitRate			{Rate/Einheit}%
	\def\Fees			{Honorare}%
	\def\VAT			{MWSt.}%
	\def\Expenses			{Auslagen}%
	\def\SumFees			{Summe \Fees}%
	\def\SumVAT			{Summe \VAT}%
	\def\SumExpenses		{Summe \Expenses}%
	\def\SubtotalFee		{Zwischensumme \Fees}%
	\def\SubtotalExpenses		{Zwischensumme \Expenses}%
	\def\SubtotalProject		{Zwischensumme \Project}%
	\def\Total			{Gesamtsumme}%
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is New German.
%
\ifx\l@ngerman\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@ngerman\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@ngerman
	\def\Warning			{Warnung}%
	\def\Error			{Fehler}%
	\def\Expense			{Auslage}%
	\def\Amount			{Betrag}%
	\def\Currency			{W\"ahrung}%
	\def\Factor			{Faktor}%
	\def\Activity			{Aktivit\"at}%
	\def\Count			{Anzahl}%
	\def\UnitRate			{Rate/Einheit}%
	\def\Fees			{Honorare}%
	\def\VAT			{MWSt.}%
	\def\Expenses			{Auslagen}%
	\def\SumFees			{Summe \Fees}%
	\def\SumVAT			{Summe \VAT}%
	\def\SumExpenses		{Summe \Expenses}%
	\def\SubtotalFee		{Zwischensumme \Fees}%
	\def\SubtotalExpenses		{Zwischensumme \Expenses}%
	\def\SubtotalProject		{Zwischensumme \Project}%
	\def\Total			{Gesamtsumme}%
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is Italian.
%
\ifx\l@italian\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@italian\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@italian
	\def\Warning			{Avvertenza}%
	\def\Error			{Errore}%
	\def\Expense			{Spesa}%
	\def\Amount			{Ammontare}%
	\def\Currency			{Valuta}%
	\def\Factor			{Fattore}%
	\def\Activity			{Attivit\`a}%
	\def\Count			{Quantit\`a}%
	\def\UnitRate			{Prezzo/Unit\`a}%
	\def\Fees			{Onorario}%
	\def\VAT			{IVA}%
	\def\Expenses			{Spese}%
	\def\SumFees			{Totale onorario}%
	\def\SumVAT			{Totale IVA}%
	\def\SumExpenses		{Totale spese}%
	\def\SubtotalFee		{Subtotale onorario}%
	\def\SubtotalExpenses		{Subtotale spese}%
	\def\SubtotalProject		{Subtotale progetto}%
	\def\Total			{Totale}%
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is Spanish I.
%
\ifx\l@spanish\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@spanish\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@spanish
	\def\Warning			{Advertencia}
	\def\Error			{Error}
	\def\Expense			{Gasto}
	\def\Amount			{Cantidad}
	\def\Currency			{Divisa}
	\def\Factor			{Factor}
	\def\Activity			{Actividad}
	\def\Count			{Cuant\'ia}
	\def\UnitRate			{Precio/Unidad}
	\def\Fees			{Honorario}
	\def\VAT			{IVA}
	\def\Expenses			{Gastos}
	\def\SumFees			{Total de honorarios}
	\def\SumVAT			{Total IVA}
	\def\SumExpenses		{Total de gastos}
	\def\SubtotalFee		{Subtotal de honorarios}
	\def\SubtotalExpenses		{Subtotal de gastos}
	\def\SubtotalProject		{Subtotal del proyecto}
	\def\Total			{Total}
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is Spanish II.
%
\ifx\l@spanishe\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@spanishe\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@spanishe
	\def\Warning			{Advertencia}
	\def\Error			{Error}
	\def\Expense			{Expensa}
	\def\Amount			{Monto}
	\def\Currency			{Moneda}
	\def\Factor			{Factor}
	\def\Activity			{Actividad}
	\def\Count			{Cantidad}
	\def\UnitRate			{Precio unitario}
	\def\Fees			{Pago} %
	\def\VAT			{IVA} %
	\def\Expenses			{Expensas} %
	\def\SumFees			{Total a pagar}
	\def\SumVAT			{Total IVA}
	\def\SumExpenses		{Total expensas}
	\def\SubtotalFee		{Subtotal a pagar}
	\def\SubtotalExpenses		{Subtotal expensas}
	\def\SubtotalProject		{Subtotal proyecto}
	\def\Total			{Total}
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is Spanish III
%
\ifx\l@spanishv\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@spanishv\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@spanishv
	\def\Warning			{Advertencia}
	\def\Error			{Error}
	\def\Expense			{Gasto}
	\def\Amount			{Importe}
	\def\Currency			{Divisa}
	\def\Factor			{Factor}
	\def\Activity			{Actividad}
	\def\Count			{Cantidad}
	\def\UnitRate			{Precio por unidad}
	\def\Fees			{Honorarios} %
	\def\VAT			{IVA} %
	\def\Expenses			{Gastos} %
	\def\SumFees			{Honorarios totales}
	\def\SumVAT			{Total IVA}
	\def\SumExpenses		{Gastos totales}
	\def\SubtotalFee		{Subtotal de honorarios}
	\def\SubtotalExpenses		{Subtotal de gastos}
	\def\SubtotalProject		{Subtotal del proyecto}
	\def\Total			{Total}
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is Swedish.
%
\ifx\l@swedish\undefined
	\message{^^J(invoice) \Warning:
		Language \string\l@swedish\space unknown.^^J^^J}
\else
\ifnum\number\invoice@language=\number\l@swedish
	\def\Warning			{Varning}%
	\def\Error			{Fel}%
	\def\Expense			{UtlÃ¤gg}%
	\def\Amount			{Belopp}%
	\def\Currency			{Valuta}%
	\def\Factor			{Faktor}%
	\def\Activity			{Aktivitet}%
	\def\Count			{Antal}%
	\def\UnitRate			{Pris/Enhet}%
	\def\Fees			{Arvoden}%
	\def\VAT			{Moms}%
	\def\Expenses			{UtlÃ¤gg}%
	\def\SumFees			{Summa \Fees}%
	\def\SumVAT			{Summa \VAT}%
	\def\SumExpenses		{Summa \Expenses}%
	\def\SubtotalFee		{Mellansumma \Fees}%
	\def\SubtotalExpenses		{Mellansumma \Expenses}%
	\def\SubtotalProject		{Mellansumma \Project}%
	\def\Total			{Slutsumma}%
\fi\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% How to add new label languages to the `invoice' package:
%
% 1. Copy all following lines after this explanation
%    and insert them above this comment.
%
% 2. Remove all comment symbols at the beginning of the lines.
%
% 3. Fill the empty parentheses {} with the appropriate
%    translations.
%
% 4. Enter the correct internal language name used by LaTeX2e
%    into the condition of the \ifnum clause.
%
% 5. Please do not forget to mail the resulting file to
%    oliver.corff@email.de
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Name correct language name here --v--
% and   --v--!
%\ifx\l@german\undefined
%	\message{^^J(invoice) \Warning:
%		Language \string\l@german\space unknown.^^J^^J}
%\else
%\ifnum\number\invoice@language=\number\l@german
%	\def\Warning			{} % Enter translations here!
%	\def\Error			{} %
%	\def\Expense			{} %
%	\def\Amount			{} %
%	\def\Currency			{} %
%	\def\Factor			{} %
%	\def\Activity			{} %
%	\def\Count			{} %
%	\def\UnitRate			{} %
%	\def\Fees			{} %
%	\def\VAT			{} %
%	\def\Expenses			{} %
%	\def\SumFees			{} %
%	\def\SumVAT			{} %
%	\def\SumExpenses		{} %
%	\def\SubtotalFee		{} %
%	\def\SubtotalExpenses		{} %
%	\def\SubtotalProject		{} %
%	\def\Total			{} %
%\fi\fi"""
