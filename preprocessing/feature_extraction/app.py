from preprocessing.feature_extraction.document_cleaning import DocumentCleaning
from preprocessing.feature_extraction.lexicon import Lexicon

text = "In den alten Zeiten, wo das Wünschen noch geholfen hat, lebte ein König, dessen Töchter waren alle schön, aber die jüngste war so schön, daß die Sonne selber, die doch so vieles gesehen hat, sich verwunderte, so oft sie ihr ins Gesicht schien. Nahe bei dem Schlosse des Königs lag ein großer dunkler Wald, und in dem Walde unter einer alten Linde war ein Brunnen; wenn nun der Tag sehr heiß war, so ging das Königskind hinaus in den Wald und setzte sich an den Rand des kühlen Brunnens, und wenn sie Langeweile hatte, so nahm sie eine goldene Kugel, warf sie in die Höhe und fing sie wieder; und das war ihr liebstes Spielwerk. Nun trug es sich einmal zu, daß die goldene Kugel der Königstochter nicht in ihr Händchen fiel, das sie in die Höhe gehalten hatte, sondern vorbei auf die Erde schlug und geradezu ins Wasser hineinrollte. Die Königstochter folgte ihr mit den Augen nach, aber die Kugel verschwand, und der Brunnen war tief, so tief, daß man keinen Grund sah. Da fing sie an zu weinen und weinte immer lauter und konnte sich gar nicht trösten. Und wie sie so klagte, rief ihr jemand zu: \"Was hast du vor, Königstochter, du schreist ja, daß sich ein Stein erbarmen möchte.\" Sie sah sich um, woher die Stimme käme, da erblickte sie einen Frosch, der seinen dicken häßlichen Kopf aus dem Wasser streckte. \"Ach, du bist's, alter Wasserpatscher,\" sagte sie, \"ich weine über meine goldene Kugel, die mir in den Brunnen hinabgefallen ist.\" \"Sei still und weine nicht,\" antwortete der Frosch, \"ich kann wohl Rat schaffen, aber was giebst du mir, wenn ich dein Spielwerk wieder heraushole?\" \"Was du haben willst, lieber Frosch,\" sagte sie, \"meine Kleider, meine Perlen und Edelsteine, auch noch die goldene Krone, die ich trage.\" "
dc = DocumentCleaning(text)
lengths = dc.build_sentence_length_vector()
words_in_document = dc.build_stemmed_word_vector()

lexicon = Lexicon()
[lexicon.add_entry(word) for word in words_in_document]
lexicon.print(1)

histo = lexicon.create_histogram()
