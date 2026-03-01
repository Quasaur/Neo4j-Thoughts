# Neo4j AuraDB vs Content Folder Discrepancy Report

**Generated:** 2026-02-28 21:41:36

## Executive Summary

| Node Type | Local Files | AuraDB Nodes | Missing in AuraDB | Missing in Local | Mismatched | In Sync |
|-----------|-------------|--------------|-------------------|------------------|------------|----------|
| THOUGHT | 319 | 215 | 130 | 26 | 12 | 177 |
| QUOTE | 81 | 77 | 6 | 2 | 0 | 75 |
| PASSAGE | 28 | 22 | 11 | 5 | 0 | 17 |
| TOPIC | 59 | 54 | 7 | 2 | 8 | 44 |

---

## 1. Nodes Missing in AuraDB (Present in Local, Missing in AuraDB)

These nodes exist in the content folder but are not present in the Neo4j AuraDB instance.

### THOUGHT Nodes Missing in AuraDB (130 total)

| Name | Alias | Parent | File | neo4j flag |
|------|-------|--------|------|------------|
| `thought.IMAGE OF GOD` | Thought: Image Of God | topic.CREATION | THOUGHTS/thought-IMAGE-OF-GOD.md | True |
| `thought.SEED DESIGN` | Thought: Seed Design | topic.BOTANY | THOUGHTS/thought-SEED-DESIGN.md | True |
| `"thought.SCIENCE_CONSPIRACY"` | Thought: SCIENCE CONSPIRACY | "topic.COSMOLOGY" | THOUGHTS/thought-SCIENCE-CONSPIRACY.md | True |
| `thought.REJOICING IN OTHERS` | Thought: Rejoicing In Others | topic.LOVE | THOUGHTS/thought-REJOICING-IN-OTHERS.md | True |
| `thought.SPECIFIED COMPLEXITY` | Thought: Specified Complexity | topic.CREATION | THOUGHTS/thought-SPECIFIED-COMPLEXITY.md | True |
| `"thought.ANTI_SEMITISM"` | Thought: ANTI-SEMITISM | "topic.PSYCHOLOGY" | THOUGHTS/thought-ANTI-SEMITISM.md | True |
| `"thought.DESPISING_THE_CROSS"` | Thought: DESPISING THE CROSS | "topic.EVIL" | THOUGHTS/thought-DESPISING-THE-CROSS.md | True |
| `thought.INTELLIGENT DESIGN` | Thought: Intelligent Design | topic.CREATION | THOUGHTS/thought-INTELLIGENT-DESIGN.md | True |
| `thought.A GREAT DAY` | Thought: A Great Day | topic.HUMOR | THOUGHTS/thought-A-GREAT-DAY.md | True |
| `thought.TEN TRILLION CELLS` | Thought: Ten Trillion Cells | topic.BIOLOGY | THOUGHTS/thought-TEN-TRILLION-CELLS.md | True |
| `thought.HOLLYWOOD VIOLENCE PREMISE` | Thought: Hollywood Violence Premise | topic.WISDOM | THOUGHTS/thought-HOLLYWOOD-VIOLENCE-PREMISE.md | True |
| `thought.DIVINE WILL` | Thought: Sovereignty of God's Will | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-DIVINE-WILL.md | True |
| `thought.EARTH SPEED SPACE` | Thought: Earth Speed Space | topic.ASTROPHYSICS | THOUGHTS/thought-EARTH-SPEED-SPACE.md | True |
| `thought.NOT LOOKING IDIOT` | Thought: Not Looking Idiot | topic.WISDOM | THOUGHTS/thought-NOT-LOOKING-IDIOT.md | True |
| `thought.OPPORTUNITY FOR ANGER` | Thought: Opportunity For Anger | topic.ATTITUDE | THOUGHTS/thought-OPPORTUNITY-FOR-ANGER.md | True |
| `thought.FAITH REQUIRES LOVE` | Thought: Faith Requires Love | topic.LOVE | THOUGHTS/thought-FAITH-REQUIRES-LOVE.md | True |
| `"thought.NO_MATCH"` | Thought: NO MATCH | "topic.BEAUTY" | THOUGHTS/thought-NO-MATCH.md | True |
| `thought.UNDERSTANDING SIN HELL` | Thought: Understanding Sin Hell | topic.EVIL | THOUGHTS/thought-UNDERSTANDING-SIN-HELL.md | True |
| `thought.CHOKING THE WORD` | Thought: Choking The Word | topic.FAITH | THOUGHTS/thought-CHOKING-THE-WORD.md | True |
| `thought.AWARENESS` | Thought: GOD AWARENESS |  | THOUGHTS/thought-AWARENESS.md | True |
| `thought.ULTIMATE2` | Thought: THE ULTIMATE (2) |  | THOUGHTS/thought-ULTIMATE2.md | True |
| `thought.MOST BEAUTIFUL GOD` | Thought: Most Beautiful God | topic.BEAUTY | THOUGHTS/thought-MOST-BEAUTIFUL-GOD.md | False |
| `thought.FAITH IN SELF VS CREATOR` | Thought: Faith In Self Vs Creator | topic.FAITH | THOUGHTS/thought-FAITH-IN-SELF-VS-CREATOR.md | True |
| `thought.CHANGING THE HEART` | Thought: Changing The Heart | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-CHANGING-THE-HEART.md | True |
| `thought.COMMUNICATION SYSTEMS` | Thought: Communication Systems | topic.COMMUNICATION THEORY | THOUGHTS/thought-COMMUNICATION-SYSTEMS.md | True |
| `thought.ANGER AS CONTAGION` | Thought: Anger As Contagion | topic.ATTITUDE | THOUGHTS/thought-ANGER-AS-CONTAGION.md | True |
| `"thought.INVITE_OR_COMMAND?"` | Thought: INVITE OR COMMAND | "topic.THE-GOSPEL" | THOUGHTS/thought-INVITE-OR-COMMAND.md | True |
| `thought.BACH AND GENIUS` | Thought: Gift of Genius | topic.MUSIC | THOUGHTS/thought-BACH-AND-GENIUS.md | True |
| `thought.DEBTORS` | Thought: DEBTORS | topic.ECONOMICS | THOUGHTS/thought-DEBTORS.md | True |
| `thought.GORGEOUS DIVINITY` | Thought: Gorgeous Divinity | topic.BEAUTY | THOUGHTS/thought-GORGEOUS-DIVINITY.md | False |
| `thought.DEFINE FAITH PERSUASION` | Thought: Define Faith Persuasion | topic.FAITH | THOUGHTS/thought-DEFINE-FAITH-PERSUASION.md | True |
| `thought.FOSSIL AMINO ACIDS` | Thought: Fossil Amino Acids | topic.GEOLOGY | THOUGHTS/thought-FOSSIL-AMINO-ACIDS.md | True |
| `thought.RESPECTING OUR BODIES` | Thought: Respecting Our Bodies | topic.ATTITUDE | THOUGHTS/thought-RESPECTING-OUR-BODIES.md | True |
| `thought.ULTIMATE` | Thought: THE ULTIMATE | topic.THE GODHEAD | THOUGHTS/thought-ULTIMATE.md | True |
| `thought.SAVED FROM GOD` | Thought: Saved From God | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-SAVED-FROM-GOD.md | True |
| `thought.EQUALITY AT RETURN` | Thought: Equality At Return | topic.SOTERIOLOGY | THOUGHTS/thought-EQUALITY-AT-RETURN.md | True |
| `thought.FAITH AND WEALTH` | Thought: Faith And Wealth | topic.WEALTH | THOUGHTS/thought-FAITH-AND-WEALTH.md | True |
| `thought.ATOMS IN CELL` | Thought: Atoms In Cell | topic.BIOLOGY | THOUGHTS/thought-ATOMS-IN-CELL.md | True |
| `thought.LUCIFERS DECEPTION` | Thought: Lucifers Deception | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-LUCIFERS-DECEPTION.md | True |
| `thought.OUTER VS INNER BEAUTY` | Thought: Outer Vs Inner Beauty | topic.ATTITUDE | THOUGHTS/thought-OUTER-VS-INNER-BEAUTY.md | False |
| `thought.END OF ALL FLESH` | Thought: End Of All Flesh | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-END-OF-ALL-FLESH.md | True |
| `thought.DEFINE APATHY` | Thought: Define Apathy | topic.ATTITUDE | THOUGHTS/thought-DEFINE-APATHY.md | True |
| `thought.ANNIHILATION OF EVIL` | Thought: Annihilation Of Evil | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-ANNIHILATION-OF-EVIL.md | True |
| `thought.MODERN PROPAGANDA` | Thought: Modern Propaganda | topic.EVIL | THOUGHTS/thought-MODERN-PROPAGANDA.md | True |
| `thought.TERRIBLE SECRETS` | Thought: Terrible Secrets | topic.PSYCHOLOGY | THOUGHTS/thought-TERRIBLE-SECRETS.md | True |
| `thought.NUTRITION MUSCLE ACHES` | Thought: Nutrition Muscle Aches | topic.HEALTH SCIENCES | THOUGHTS/thought-NUTRITION-MUSCLE-ACHES.md | True |
| `thought.WEATHER AS COMMUNICATION` | Thought: Weather As Communication | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-WEATHER-AS-COMMUNICATION.md | True |
| `thought.WANTING FORGIVENESS ONLY` | Thought: Wanting Forgiveness Only | topic.LOVE | THOUGHTS/thought-WANTING-FORGIVENESS-ONLY.md | True |
| `thought.GLOBAL ECONOMICS FOOTSTOOL` | Thought: Global Economics Footstool | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-GLOBAL-ECONOMICS-FOOTSTOOL.md | True |
| `thought.GLOVES` | Thought: GLOVES | topic.EVANGELISM | THOUGHTS/thought-GLOVES.md | True |
| `thought.ESSENCE OF JOY` | Thought: Essence Of Joy | topic.ATTITUDE | THOUGHTS/thought-ESSENCE-OF-JOY.md | True |
| `thought.FEAR AS BAD MOTIVE` | Thought: Fear As Bad Motive | topic.ATTITUDE | THOUGHTS/thought-FEAR-AS-BAD-MOTIVE.md | True |
| `thought.DEFINE FAITH WILL` | Thought: Define Faith Will | topic.FAITH | THOUGHTS/thought-DEFINE-FAITH-WILL.md | True |
| `thought.GOD IS BEAUTY` | Thought: God Is Beauty | topic.BEAUTY | THOUGHTS/thought-GOD-IS-BEAUTY.md | False |
| `thought.VISIBLE UNIVERSE` | Thought: Visible Universe | topic.COSMOLOGY | THOUGHTS/thought-VISIBLE-UNIVERSE.md | True |
| `thought.DAMNING THE ARROGANT` | Thought: Damning The Arrogant | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-DAMNING-THE-ARROGANT.md | True |
| `thought.INTELLIGENT DESIGN PROOF` | Thought: Intelligent Design Proof | topic.CREATION | THOUGHTS/thought-INTELLIGENT-DESIGN-PROOF.md | True |
| `thought.WHISPER OF HOPE` | Thought: Whisper Of Hope | topic.ATTITUDE | THOUGHTS/thought-WHISPER-OF-HOPE.md | True |
| `thought.DEBT` | Thought: DEBT | topic.ENTITLEMENT | THOUGHTS/thought-DEBT.md | True |
| `thought.NEED FOR FAITH` | Thought: Need For Faith | topic.FAITH | THOUGHTS/thought-NEED-FOR-FAITH.md | True |
| `thought.BENEFICIARIES` | Thought: BENEFICIARIES | topic.EVANGELISM | THOUGHTS/thought-BENEFICIARIES.md | True |
| `thought.GIANT BALL OF ROCK` | Thought: Giant Ball Of Rock | topic.CREATION | THOUGHTS/thought-GIANT-BALL-OF-ROCK.md | True |
| `"thought.GOD_IN_CHARGE"` | Thought: GOD IN CHARGE | "topic.DIVINE-SOVEREIGNTY" | THOUGHTS/thought-GOD-IN-CHARGE.md | True |
| `thought.HEAVY DIVINE WILL` | Thought: Heavy Divine Will | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-HEAVY-DIVINE-WILL.md | True |
| `thought.PERFECT PEOPLE CRITICISM` | Thought: Perfect People Criticism | topic.ATTITUDE | THOUGHTS/thought-PERFECT-PEOPLE-CRITICISM.md | True |
| `thought.JESUS THE MONARCH` | Thought: Jesus The Monarch | topic.POLITICAL SCIENCE | THOUGHTS/thought-JESUS-THE-MONARCH.md | True |
| `"thought.WHEN_JESUS_RETURNS"` | Thought: WHEN JESUS RETURNS | "topic.HISTORY" | THOUGHTS/thought-WHEN-JESUS-RETURNS.md | True |
| `thought.LIGHTNING BOLT` | Thought: Lightning Bolt | topic.ENVIRONMENTAL SCIENCE | THOUGHTS/thought-LIGHTNING-BOLT.md | True |
| `thought.HONESTY THROUGH LOVE` | Thought: Honesty Through Love | topic.LOVE | THOUGHTS/thought-HONESTY-THROUGH-LOVE.md | True |
| `thought.ATTENTION DESIRE` | Thought: Attention Desire | topic.ATTITUDE | THOUGHTS/thought-ATTENTION-DESIRE.md | True |
| `thought.BOX JELLYFISH EYES` | Thought: Box Jellyfish Eyes | topic.BIOLOGY | THOUGHTS/thought-BOX-JELLYFISH-EYES.md | True |
| `thought.HOLY-SPIRIT` | Thought: THE HOLY SPIRIT | topic.THE GODHEAD | THOUGHTS/thought-HOLY-SPIRIT.md | True |
| `thought.GOD THE RECYCLER` | Thought: God The Recycler | topic.ENVIRONMENTAL SCIENCE | THOUGHTS/thought-GOD-THE-RECYCLER.md | True |
| `thought.LUCIFERS WRETCHEDNESS` | Thought: Lucifers Wretchedness | topic.EVIL | THOUGHTS/thought-LUCIFERS-WRETCHEDNESS.md | True |
| `thought.TWO GARDENS` | Thought: Two Gardens | topic.SOTERIOLOGY | THOUGHTS/thought-TWO-GARDENS.md | True |
| `thought.SUN ENERGY` | Thought: Sun Energy | topic.ASTROPHYSICS | THOUGHTS/thought-SUN-ENERGY.md | True |
| `thought.VOICE OF THE DEVIL` | Thought: Voice Of The Devil | topic.EVIL | THOUGHTS/thought-VOICE-OF-THE-DEVIL.md | True |
| `thought.WRATH OF GOD` | Thought: Wrath Of God | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-WRATH-OF-GOD.md | True |
| `thought.DEFINING EVIL PRIDE` | Thought: Defining Evil Pride | topic.EVIL | THOUGHTS/thought-DEFINING-EVIL-PRIDE.md | True |
| `thought.ENDING` | Thought: ENDING | topic.APOCALYPSE | THOUGHTS/thought-ENDING.md | True |
| `thought.UNREASONABLE PEOPLE PROBLEM` | Thought: Unreasonable People Problem | topic.WISDOM | THOUGHTS/thought-UNREASONABLE-PEOPLE-PROBLEM.md | True |
| `"thought.THE_QUICK_AND_THE_DEAD"` | Thought: THE QUICK AND THE DEAD | "topic.SPIRITUALITY" | THOUGHTS/thought-THE-QUICK-AND-THE-DEAD.md | True |
| `thought.NO ANGER SELFLESSNESS` | Thought: No Anger Selflessness | topic.ATTITUDE | THOUGHTS/thought-NO-ANGER-SELFLESSNESS.md | True |
| `thought.PRIDE OF SATAN` | Thought: Pride Of Satan | topic.EVIL | THOUGHTS/thought-PRIDE-OF-SATAN.md | True |
| `thought.JUDGMENT OF NATIONS` | Thought: Judgment Of Nations | topic.APOCALYPSE | THOUGHTS/thought-JUDGMENT-OF-NATIONS.md | True |
| `thought.ELECTROMAGNETISM TOUCH` | Thought: Electromagnetism Touch | topic.PHYSICS | THOUGHTS/thought-ELECTROMAGNETISM-TOUCH.md | True |
| `thought.IRREDUCIBLE COMPLEXITY` | Thought: Irreducible Complexity | topic.CREATION | THOUGHTS/thought-IRREDUCIBLE-COMPLEXITY.md | True |
| `thought.SUNS ENERGY CORE` | Thought: Suns Energy Core | topic.ASTROPHYSICS | THOUGHTS/thought-SUNS-ENERGY-CORE.md | True |
| `thought.DEFINE EVIL JEALOUSY` | Thought: Define Evil Jealousy | topic.EVIL | THOUGHTS/thought-DEFINE-EVIL-JEALOUSY.md | True |
| `thought.SHOULD BE VS WILL BE` | Thought: Should Be Vs Will Be | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-SHOULD-BE-VS-WILL-BE.md | True |
| `thought.DESTROYING THE EARTH` | Thought: Destroying The Earth | topic.ENVIRONMENTAL SCIENCE | THOUGHTS/thought-DESTROYING-THE-EARTH.md | True |
| `thought.FATHER` | Thought: FATHER | topic.GRACE | THOUGHTS/thought-FATHER.md | True |
| `thought.ORDERS GIVING TAKING` | Thought: Orders Giving Taking | topic.WISDOM | THOUGHTS/thought-ORDERS-GIVING-TAKING.md | True |
| `thought.ROYAL_DIET` | Thought: DIET01 | topic.HEALTH | THOUGHTS/thought-ROYAL-DIET.md | True |
| `thought.CHANGE OTHERS NOT SELF` | Thought: Change Others Not Self | topic.ATTITUDE | THOUGHTS/thought-CHANGE-OTHERS-NOT-SELF.md | True |
| `thought.CITIZENSHIP` | Thought: CITIZENSHIP | topic.ECONOMICS | THOUGHTS/thought-CITIZENSHIP.md | True |
| `"thought.THE_REAL_YOU"` | Thought: THE REAL YOU | "topic.GRACE" | THOUGHTS/thought-THE-REAL-YOU.md | True |
| `"thought.SHUT_DOWN"` | Thought: SHUT DOWN | "topic.FREEDOM" | THOUGHTS/thought-SHUT-DOWN.md | True |
| `thought.WITHHOLDING POWERS` | Thought: Withholding Powers | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-WITHHOLDING-POWERS.md | True |
| `thought.EARTH STORMS` | Thought: Earth Storms | topic.ASTROPHYSICS | THOUGHTS/thought-EARTH-STORMS.md | True |
| `thought.FAITH IN EVOLUTION` | Thought: Faith In Evolution | topic.PHILOSOPHY | THOUGHTS/thought-FAITH-IN-EVOLUTION.md | True |
| `thought.FAITH AND ACCEPTANCE` | Thought: Faith And Acceptance | topic.FAITH | THOUGHTS/thought-FAITH-AND-ACCEPTANCE.md | True |
| `"thought.MARK_OF_THE_BEAST"` | Thought: MARK OF THE BEAST | "topic.THE-GOSPEL" | THOUGHTS/thought-MARK-OF-THE-BEAST.md | True |
| `"thought.OBLIVION"` | Thought: OBLIVION | "topic.HISTORY" | THOUGHTS/thought-OBLIVION.md | True |
| `thought.GOD AND EVIL` | Thought: God And Evil | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-GOD-AND-EVIL.md | True |
| `thought.LIMITLESS DIVINE POWER` | Thought: Limitless Divine Power | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-LIMITLESS-DIVINE-POWER.md | True |
| `thought.HAPPY IF GOD PLEASED` | Thought: Happy If God Pleased | topic.WORSHIP | THOUGHTS/thought-HAPPY-IF-GOD-PLEASED.md | True |
| `thought.DEFINE HOPE` | Thought: Define Hope | topic.ATTITUDE | THOUGHTS/thought-DEFINE-HOPE.md | True |
| `thought.GOD` | Thought: IMPERSONAL GOD |  | THOUGHTS/thought-GOD.md | True |
| `thought.PRIDE IS PRISON` | Thought: Pride Is Prison | topic.EVIL | THOUGHTS/thought-PRIDE-IS-PRISON.md | True |
| `thought.GOD'S WILL IN ME` | Thought: God's Will In Me | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-GOD-S-WILL-IN-ME.md | True |
| `thought.PROVING CREATION` | Thought: Proving Creation | topic.CREATION | THOUGHTS/thought-PROVING-CREATION.md | True |
| `thought.CAT LICK NECK` | Thought: Cat Lick Neck | topic.BIOLOGY | THOUGHTS/thought-CAT-LICK-NECK.md | True |
| `thought.APOCALYPSE BETTER WORLD` | Thought: Apocalypse Better World | topic.APOCALYPSE | THOUGHTS/thought-APOCALYPSE-BETTER-WORLD.md | True |
| `thought.DEFINE EXQUISITAGIOUS` | Thought: Define Exquisitagious | topic.LINGUISTICS | THOUGHTS/thought-DEFINE-EXQUISITAGIOUS.md | False |
| `"thought.ONE_REASON"` | Thought: ONE REASON | "topic.ATTITUDE" | THOUGHTS/thought-ONE-REASON.md | True |
| `thought.MODIFIED_GOSPEL` | Thought: MODIFIED GOSPEL | topic.THE-GOSPEL | THOUGHTS/thought-MODIFIED-GOSPEL.md | True |
| `thought.APPEARING HUMAN` | Thought: Appearing Human | topic.EVIL | THOUGHTS/thought-APPEARING-HUMAN.md | True |
| `thought.CAT ON KNEE` | Thought: Cat On Knee | topic.BIOLOGY | THOUGHTS/thought-CAT-ON-KNEE.md | True |
| `thought.FAITH AND SCIENCE` | Thought: Faith And Science | topic.PHYSICS | THOUGHTS/thought-FAITH-AND-SCIENCE.md | True |
| `thought.UNREASONABLE PRIDE` | Thought: Unreasonable Pride | topic.EVIL | THOUGHTS/thought-UNREASONABLE-PRIDE.md | True |
| `thought.OVERCOMING FEAR BLAME` | Thought: Overcoming Fear Blame | topic.ATTITUDE | THOUGHTS/thought-OVERCOMING-FEAR-BLAME.md | True |
| `"thought.EVIL_WAS_NECESSARY"` | Thought: EVIL WAS NECESSARY | "topic.EVIL" | THOUGHTS/thought-EVIL-WAS-NECESSARY.md | True |
| `thought.GETTING VS BEING` | Thought: Getting Vs Being | topic.WISDOM | THOUGHTS/thought-GETTING-VS-BEING.md | True |
| `thought.HUMAN BREATHS DAILY` | Thought: Human Breaths Daily | topic.BIOLOGY | THOUGHTS/thought-HUMAN-BREATHS-DAILY.md | True |
| `thought.WANTING LOVE ONLY` | Thought: Wanting Love Only | topic.LOVE | THOUGHTS/thought-WANTING-LOVE-ONLY.md | True |
| `thought.BORED VS BORING` | Thought: Bored Vs Boring | topic.ATTITUDE | THOUGHTS/thought-BORED-VS-BORING.md | True |
| `thought.REMEMBERING VS LIVING PAST` | Thought: Remembering Vs Living Past | topic.WISDOM | THOUGHTS/thought-REMEMBERING-VS-LIVING-PAST.md | True |
| `thought.GLORIFIED IN HUMANITY` | Thought: Glorified In Humanity | topic.DIVINE SOVEREIGNTY | THOUGHTS/thought-GLORIFIED-IN-HUMANITY.md | True |
| `thought.HORDES OF THE ABYSS` | Thought: Hordes Of The Abyss | topic.APOCALYPSE | THOUGHTS/thought-HORDES-OF-THE-ABYSS.md | True |

### QUOTE Nodes Missing in AuraDB (6 total)

| Name | Alias | Parent | File | neo4j flag |
|------|-------|--------|------|------------|
| `quote.FEELINGS` | Quote: Quote: FEELINGS | topic.FAITH | QUOTES/imm/quote-FEELINGS.md | True |
| `quote.THE_VALUE_OF_FAITH` | Quote: Quote: THE VALUE OF FAITH | topic.FAITH | QUOTES/imm/quote-THE-VALUE-OF-FAITH.md | False |
| `"quote.BEGOTTEN"` | Quote: God's Only Son | "topic.THE GOSPEL" | QUOTES/bom/quote-BEGOTTEN.md | True |
| `quote.LOGICAL_COURSE` | Quote: Quote: LOGICAL COURSE | topic.FAITH | QUOTES/osas/quote-LOGICAL-COURSE.md | True |
| `quote.ETERNAL_DAMNATION` | Quote: Quote: ETERNAL DAMNATION | topic.APOCALYPSE | QUOTES/tnw/quote-ETERNAL-DAMNATION.md | True |
| `quote.FAITH-FOCUSED` | Quote: Quote: FAITH-FOCUSED | topic.FAITH | QUOTES/tnw/quote-FAITH-FOCUSED.md | True |

### PASSAGE Nodes Missing in AuraDB (11 total)

| Name | Alias | Parent | File | neo4j flag |
|------|-------|--------|------|------------|
| `"passage.HONOR GOD"` | Passage: Add Offerings and Charity to your Budget | "topic.WEALTH" | PASSAGES/Prov/03/passage-HONOR-GOD.md | True |
| `"passage.KINDNESS AND TRUTH"` | Passage: The Keys to Favor and a Good Reputation | "topic.ATTITUDE" | PASSAGES/Prov/03/passage-KINDNESS-AND-TRUTH.md | True |
| `"passage.PRICELESS WISDOM"` | Passage: The Greatest Treasure | "topic.WISDOM" | PASSAGES/Prov/03/passage-PRICELESS-WISDOM.md | True |
| `"passage.INHERITED HONOR"` | Passage: HONOR AND DISGRACE | "topic.WISDOM" | PASSAGES/Prov/03/passage-INHERITED-HONOR.md | True |
| `passage.TRUST_THE_LORD` | Passage: 'Passage: TRUST THE LORD' | topic.FAITH | PASSAGES/Prov/03/passage-TRUST-THE-LORD.md | True |
| `"passage.SECURITY (2)"` | Passage: Wisdom and Discretion | "topic.WISDOM" | PASSAGES/Prov/03/passage-SECURITY-2.md | True |
| `passage.THE SOURCE OF WISDOM` | Passage: THE SOURCE OF WISDOM | topic.WISDOM | PASSAGES/Prov/02/passage-THE-SOURCE-OF-WISDOM.md | False |
| `passage.NOT-OF-FAITH` | Passage: NOT-OF-FAITH | topic.FAITH | PASSAGES/Roma/passage-NOT-OF-FAITH.md | True |
| `passage.REMOVING ALL THINGS` | Passage: Removing All Things | topic.DIVINE SOVEREIGNTY | PASSAGES/zeph/passage-REMOVING-ALL-THINGS.md | True |
| `passage.FAMILIAR SPIRITS WARNING` | Passage: Familiar Spirits Warning | topic.EVIL | PASSAGES/levi/passage-FAMILIAR-SPIRITS-WARNING.md | True |
| `passage.THE LORD GIVES` | Passage: The Rights of God. | topic.DIVINE SOVEREIGNTY | PASSAGES/job/passage-THE-LORD-GIVES.md | True |

### TOPIC Nodes Missing in AuraDB (7 total)

| Name | Alias | Parent | File | neo4j flag |
|------|-------|--------|------|------------|
| `topic.POLITICAL SCIENCE` | Topic: Politics | topic.SOCIAL SCIENCES | TOPICS/topic-POLITICAL-SCIENCE.md | True |
| `topic.ENTITLEMENT` | Topic: Arrogance | topic.ATTITUDE | TOPICS/topic-ENTITLEMENT.md | True |
| `topic.ECONOMICS` | Topic: Commerce | topic.HUMANITY | TOPICS/topic-ECONOMICS.md | True |
| `topic.EVANGELISM` | Topic: Fishers of Men | topic.THE-GOSPEL | TOPICS/topic-EVANGELISM.md | True |
| `"topic.NULL TOPIC"` | Topic: Topic ZERO: THE NULL TOPIC | null | TOPICS/topic-NULL-TOPIC.md | True |
| `topic.BEAUTY` | Topic: Beauty of Body or Character | topic.HEALTH | TOPICS/topic-BEAUTY.md | True |
| `topic.APOCALYPSE` | Topic: ESCHATOLOGY | topic.HISTORY | TOPICS/topic-APOCALYPSE.md | True |

---

## 2. Nodes Missing in Local Content (Present in AuraDB, Missing in Local)

These nodes exist in Neo4j AuraDB but are not present in the content folder.

### THOUGHT Nodes Missing in Local (26 total)

| Name | Alias | Parent |
|------|-------|--------|
| `thought.IMPERSONAL GOD` | Thought: The Genie God | topic.THE GODHEAD |
| `thought.GOD-AWARENESS` | Thought: The God Who is Here | topic.THE GODHEAD |
| `thought.THE HOLY SPIRIT` | Thought: The Most High | topic.THE GODHEAD |
| `thought.THE ULTIMATE` | Thought: The Living God | topic.THE GODHEAD |
| `thought.THE ULTIMATE (2)` | Thought: The Beginning and The End | topic.THE GODHEAD |
| `thought.692,189` | Thought: What is the Body of Christ Doing about the Mass Shootings??? | topic.PSYCHOLOGY |
| `thought.ANTI_SEMITISM` | Thought: ANTI-SEMITISM | topic.PSYCHOLOGY |
| `thought.A_GREAT_DAY` | Thought: A Great Day | topic.HUMOR |
| `thought.DESPISING_THE_CROSS` | Thought: DESPISING THE CROSS | topic.EVIL |
| `thought.EVIL_WAS_NECESSARY` | Thought: EVIL WAS NECESSARY | topic.EVIL |
| `thought.INTELLIGENT_DESIGN` | Thought: INTELLIGENT DESIGN | topic.COSMOLOGY |
| `thought.OBLIVION` | Thought: OBLIVION | topic.HISTORY |
| `thought.ONE_REASON` | Thought: ONE REASON | topic.ATTITUDE |
| `thought.SCIENCE_CONSPIRACY` | Thought: SCIENCE CONSPIRACY | topic.COSMOLOGY |
| `thought.SHUT_DOWN` | Thought: SHUT DOWN | topic.FREEDOM |
| `thought.THE_QUICK_AND_THE_DEAD` | Thought: THE QUICK AND THE DEAD | topic.SPIRITUALITY |
| `thought.THE_REAL_YOU` | Thought: THE REAL YOU | topic.GRACE |
| `thought.WHEN_JESUS_RETURNS` | Thought: WHEN JESUS RETURNS | topic.HISTORY |
| `thought.GOD_IN_CHARGE` | Thought: GOD IN CHARGE | topic.DIVINE-SOVEREIGNTY |
| `thought.INVITE_OR_COMMAND?` | Thought: INVITE OR COMMAND | topic.THE-GOSPEL |
| `thought.MARK_OF_THE_BEAST` | Thought: MARK OF THE BEAST | topic.THE-GOSPEL |
| `thought.GOD_AWARENESS` | Thought: GOD AWARENESS | topic.THE-GODHEAD |
| `thought.IMPERSONAL_GOD` | Thought: IMPERSONAL GOD | topic.THE-GODHEAD |
| `thought.THE_HOLY_SPIRIT` | Thought: THE HOLY SPIRIT | topic.THE-GODHEAD |
| `thought.THE_ULTIMATE` | Thought: THE ULTIMATE | topic.THE-GODHEAD |
| `thought.THE_ULTIMATE2` | Thought: THE ULTIMATE (2) | topic.THE-GODHEAD |

### QUOTE Nodes Missing in Local (2 total)

| Name | Alias | Parent |
|------|-------|--------|
| `quote.BEGOTTEN` | Quote: God's Only Son | topic.THE GOSPEL |
| `quote.SALVATION` | Quote: Quote: SALVATION | topic.THE-GOSPEL |

### PASSAGE Nodes Missing in Local (5 total)

| Name | Alias | Parent |
|------|-------|--------|
| `passage.KINDNESS AND TRUTH` | Passage: The Keys to Favor and a Good Reputation | topic.ATTITUDE |
| `passage.HONOR GOD` | Passage: Add Offerings and Charity to your Budget | topic.WEALTH |
| `passage.INHERITED HONOR` | Passage: Honor and Disgrace | topic.WISDOM |
| `passage.PRICELESS WISDOM` | Passage: The Greatest Treasure | topic.WISDOM |
| `passage.SECURITY (2)` | Passage: Wisdom and Discretion | topic.WISDOM |

### TOPIC Nodes Missing in Local (2 total)

| Name | Alias | Parent |
|------|-------|--------|
| `topic.NULL TOPIC` | Topic: NULL TOPIC | None |
| `topic.POLITICAL-SCIENCE` | Topic Political Theory | topic.HUMANITY |

---

## 3. Mismatched Nodes (Present in Both, But with Differences)

These nodes exist in both locations but have differing properties.

### THOUGHT Mismatched Nodes (12 total)

**`thought.MOTION`**
- File: THOUGHTS/thought-MOTION.md
- alias: local='Thought: MOTION' vs auradb='Thought: Movement'
- parent: local='' vs auradb='topic.THE GODHEAD'

**`thought.ANOTHER_SINNER`**
- File: THOUGHTS/thought-ANOTHER-SINNER.md
- alias: local='Thought: Another Sinner' vs auradb='Thought: ANOTHER SINNER'

**`thought.MEEK`**
- File: THOUGHTS/thought-MEEK.md
- alias: local='Thought: MEEK' vs auradb='Thought: The Meek God'
- parent: local='' vs auradb='topic.THE GODHEAD'

**`thought.THE_END_OF_EVIL`**
- File: THOUGHTS/thought-THE-END-OF-EVIL.md
- alias: local='Thought: THE END OF EVIL' vs auradb='Thought: The End of Evil'

**`thought.INSATIABLE`**
- File: THOUGHTS/thought-INSATIABLE.md
- alias: local='Thought: Insatiable' vs auradb='Thought: Instatiable'

**`thought.EMPTINESS`**
- File: THOUGHTS/thought-EMPTINESS.md
- alias: local='Thought: Emptiness' vs auradb='Thought: The Void Within'

**`thought.PROTECTION`**
- File: THOUGHTS/thought-PROTECTION.md
- alias: local='Thought: PROTECTION' vs auradb='Thought: Strong Tower'
- parent: local='' vs auradb='topic.THE GODHEAD'

**`thought.EGO`**
- File: THOUGHTS/thought-EGO.md
- alias: local='Thought: EGO' vs auradb='Thought: The Greatness of God'
- parent: local='' vs auradb='topic.THE GODHEAD'

**`thought.COWARDS`**
- File: THOUGHTS/thought-COWARDS.md
- parent: local='' vs auradb='topic.EVIL'

**`thought.SHOCKED`**
- File: THOUGHTS/thought-SHOCKED.md
- alias: local='Thought: Shocked' vs auradb='Thought: SHOCKED'

**`thought.MIRACLES`**
- File: THOUGHTS/thought-MIRACLES.md
- alias: local='Thought: MIRACLES' vs auradb='Thought: Acts of God'
- parent: local='' vs auradb='topic.THE GODHEAD'

**`thought.BUNYANS MASTERPIECE`**
- File: THOUGHTS/thought-BUNYANS-MASTERPIECE.md
- alias: local='Thought: Law and Grace' vs auradb='Thought: BUNYANS MASTERPIECE'

### TOPIC Mismatched Nodes (8 total)

**`topic.THE GODHEAD`**
- File: TOPICS/topic-THE-GODHEAD.md
- parent: local='topic.NULL TOPIC' vs auradb='NULL TOPIC'

**`topic.HUMANITY`**
- File: TOPICS/topic-HUMANITY.md
- parent: local='topic.CREATION' vs auradb='topic.THE GODHEAD'

**`topic.COMMUNICATION THEORY`**
- File: TOPICS/topic-COMMUNICATION-THEORY.md
- alias: local='Topic: Mankind' vs auradb='Topic: Information Sharing'

**`topic.SPIRITS`**
- File: TOPICS/topic-SPIRITS.md
- alias: local='Topic: Topic Children of the Holy Spirit' vs auradb='Topic Children of the Holy Spirit'

**`topic.GEOLOGY`**
- File: TOPICS/topic-GEOLOGY.md
- alias: local='Topic: Topic Rock Strata' vs auradb='Topic Rock Strata'

**`topic.SOCIOLOGY`**
- File: TOPICS/topic-SOCIOLOGY.md
- parent: local='topic.SOCIAL SCIENCES' vs auradb='topic.HUMANITY'

**`topic.GRACE`**
- File: TOPICS/topic-GRACE.md
- alias: local='Topic: Topic Gospel of Grace' vs auradb='Topic Gospel of Grace'

**`topic.ASTROPHYSICS`**
- File: TOPICS/topic-ASTROPHYSICS.md
- alias: local='Topic: The Physics of Astronomy' vs auradb='Topic: This History of Humanity's World Views'

---

## 4. Detailed Node Lists

### 4.1 THOUGHT Nodes

**Local THOUGHT nodes:** 319
**AuraDB THOUGHT nodes:** 215

### 4.2 QUOTE Nodes

**Local QUOTE nodes:** 81
**AuraDB QUOTE nodes:** 77

### 4.3 PASSAGE Nodes

**Local PASSAGE nodes:** 28
**AuraDB PASSAGE nodes:** 22

### 4.4 TOPIC Nodes

**Local TOPIC nodes:** 59
**AuraDB TOPIC nodes:** 54

---

## Recommendations

Based on the discrepancy analysis:

1. **Sync to AuraDB:** 154 node(s) need to be inserted into Neo4j AuraDB.
2. **Create Local Files:** 35 node(s) exist only in AuraDB and need local markdown files.
3. **Resolve Mismatches:** 20 node(s) have property differences that need reconciliation.

---

*Report generated by generate_auradb_report.py*
