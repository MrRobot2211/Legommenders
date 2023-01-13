from model_v2.operator.ada_operator import AdaOperator
from model_v2.operator.attention_operator import AttentionOperator
from model_v2.operator.transformer_operator import TransformerOperator
from model_v2.recommenders.base_neg_recommender import BaseNegRecommender


class PLMNRNAMLModel(BaseNegRecommender):
    news_encoder_class = TransformerOperator
    user_encoder_class = AdaOperator
